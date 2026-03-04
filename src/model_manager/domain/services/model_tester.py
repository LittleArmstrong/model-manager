from ultralytics import YOLO
from ultralytics.models.yolo.detect.val import DetectionValidator
from model_manager.domain.models.dataset import YoloDataset
from collections import defaultdict
from ultralytics.utils.nms import TorchNMS
import torch
import math 
from model_manager.domain.evaluator import calc_f1_score
from model_manager.repository.dataset_reader import DatasetReader
from dataclasses import dataclass, field, fields
from typing import Optional, Callable, List
from ultralytics.models.yolo.detect import DetectionValidator
from model_manager.domain.services.model_storage import YoloModelStorage
from pathlib import Path


@dataclass(frozen=True)
class EvalConfig:
    # imgsz: int = 640
    batch: int = 16
    min_conf: float = 0.25
    min_nms_iou: float = 0.7



@dataclass
class EvalCallbacks:
    on_val_start:Optional[List[Callable[[DetectionValidator], None]]] = field(default_factory=list)
    on_val_batch_start:Optional[List[Callable[[DetectionValidator], None]]] = field(default_factory=list)
    on_val_batch_end:Optional[List[Callable[[DetectionValidator], None]]] = field(default_factory=list)
    on_val_end:Optional[List[Callable[[object, object, str], None]]] = field(default_factory=list)

    def __post_init__(self):
        for f in fields(self):
            val = getattr(self, f.name)
            if val is None:
                setattr(self, f.name, [])

    def fire(self, name: str, *args, **kwargs):
        for cb in getattr(self, name):
            cb(*args, **kwargs)

@dataclass
class EvalResult:
    metrics: list[dict]
    predictions: list[dict]
    classes: list[str]
    img_path: Path


class YoloModelTester:

    @classmethod
    def test(
        cls,
        model: YOLO,
        dataset: YoloDataset,
        config: EvalConfig=None,
        callbacks: EvalCallbacks = None,
        validator: DetectionValidator | None = None
    ):
        if not config:
            config = EvalConfig()

        # args exakt so bauen wie Ultralytics es erwartet
        if not validator:
            custom = {"rect": True}
            kwargs = {
                "data": dataset.yaml_path,
                # "imgsz": config.imgsz,
                "batch": config.batch,
                "save_json": True,
                "plots": False,
                "split": "test",
                # "project": YoloModelStorage.TESTING_PROJECT,
                # "name": YoloModelStorage.TESTING_NAME,
                "save_dir": (YoloModelStorage.TESTING_PROJECT/YoloModelStorage.TESTING_NAME).resolve(),
                "verbose": False,
                "save_txt": False,
                "save_conf": False,
                "visualize": False,
                "exist_ok": True,
            }

            args = {
                **model.overrides,
                **custom,
                **kwargs,
                "mode": "val",
            }  
            validator = DetectionValidator(
                args=args
            )

        # Werte für Progress berechnen
        num_test_imgs = DatasetReader(dataset).count_images(split="test")
        total_batches = math.ceil(num_test_imgs / config.batch)

        # Callbacks hinzufügen
        if not callbacks:
            callbacks = EvalCallbacks()

        for field in fields(callbacks):
            if field.name == "on_val_end":
                # wird später manuell aufgerufen
                continue
            func_list = getattr(callbacks, field.name)
            # total batches für progress hinzufügen
            if field.name == "on_val_batch_end":
                func_list = [cls._wrap_batch_end(func, total_batches) for func in func_list]
            validator.callbacks[field.name].extend(func_list)

        # Evaluation
        validator(model=model.model)

        # Datenaufbereitung
        yolo_results = validator.metrics
        class_results = yolo_results.to_df().rows(named=True)
        aggregate = {
            "Class": "Gesamt",
            "Images": num_test_imgs,
            "Instances": sum(int(r["Instances"]) for r in class_results),
            "Box-P": round(yolo_results.results_dict["metrics/precision(B)"], 5),
            "Box-R": round(yolo_results.results_dict["metrics/recall(B)"], 5),
            "Box-F1": round(
                calc_f1_score(
                    yolo_results.results_dict["metrics/precision(B)"],
                    yolo_results.results_dict["metrics/recall(B)"]
                ), 5
            ),
            "mAP50": round(yolo_results.results_dict["metrics/mAP50(B)"], 5),
            "mAP50-95": round(yolo_results.results_dict["metrics/mAP50-95(B)"], 5),
        }
        full_results = [aggregate] + class_results


        predictions = cls._postprocess_predictions(validator.jdict, min_conf=config.min_conf, min_nms_iou=config.min_nms_iou)
        metrics = EvalResult( 
            metrics=full_results,
            predictions=predictions,
            classes=model.names,
            img_path=dataset.test_images,
        )
        callbacks.fire("on_val_end", metrics)
        return metrics
    
        

    @classmethod
    def _postprocess_predictions(cls, pred_list: list[dict], min_conf: float, min_nms_iou:float):
        grouped = defaultdict(lambda: {
            "file_name": None,
            "category_ids": [],
            "scores": [],
            "bboxes": [],
        })
        
        for p in pred_list:
            img_id = p["image_id"]
            g = grouped[img_id]
            g["file_name"] = p["file_name"]

            if p["score"] < min_conf:
                continue
            g["category_ids"].append(p["category_id"])
            g["scores"].append(p["score"])
            g["bboxes"].append(p["bbox"])

        
        grouped_predictions = defaultdict(lambda: {
            "file_name": None,
            "category_ids": [],
            "scores": [],
            "bboxes": [],
        })
        
        for img_id, prediction in grouped.items():
            g = grouped_predictions[img_id]
            g["file_name"] = prediction["file_name"]
            if not prediction["scores"]:
                continue
            
            boxes = torch.tensor([cls._coco_to_xyxy(bbox) for bbox in prediction["bboxes"]], dtype=torch.float32)
            scores = torch.tensor([score for score in prediction["scores"]], dtype=torch.float32)
            keep = TorchNMS.nms(boxes, scores, min_nms_iou)
            for idx in keep:
                idx = idx.item()  # Tensor → int
                g["category_ids"].append(prediction["category_ids"][idx])
                g["scores"].append(prediction["scores"][idx])
                g["bboxes"].append(prediction["bboxes"][idx])  


        # Scores min/max berechnen
        for img_id, g in grouped_predictions.items():
            g["min_score"] = min(g["scores"], default=0.0)
            g["max_score"] = max(g["scores"], default=0.0)

        return list(grouped_predictions.values())
    
    @staticmethod
    def _coco_to_xyxy(bbox:list):
        x, y, w, h = bbox
        return [x, y, x + w, y + h]

    @staticmethod
    def _wrap_batch_end(callback, total_batches):
        def wrapper(validator):
            callback(validator, total_batches)  
        return wrapper