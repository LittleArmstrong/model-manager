from ultralytics import YOLO
from model_manager.domain.models.dataset import YoloDataset
import math 
from model_manager.domain.evaluator import calc_f1_score
from model_manager.repository.dataset_reader import DatasetReader
from model_manager.domain.services.model_inspector import YoloModelInspector
from model_manager.domain.services.model_storage import YoloModelStorage
from ultralytics.models.yolo.detect import DetectionTrainer
from dataclasses import fields, dataclass, field
from typing import Optional, Callable, List


@dataclass(frozen=True)
class TrainingConfig:
    imgsz:int = 640
    batch: int = 16
    epochs: int = 100
    lr0:float = 0.01
    freeze: int = 10
    optimizer: str = "auto"
    weight_decay:  float = 0.0001
    resume_training: bool = False

@dataclass
class TrainingProgress:
    batches_per_epoch: int
    total_batches: int
    epochs: int
    epoch: int = 0
    batch_count: int = 0

@dataclass
class TrainingCallbacks:
    on_train_start: Optional[List[Callable[[DetectionTrainer], None]]] = field(default_factory=list)
    on_train_batch_start: Optional[List[Callable[[DetectionTrainer], None]]] = field(default_factory=list)
    on_train_batch_end: Optional[List[Callable[[DetectionTrainer, TrainingProgress], None]]] = field(default_factory=list)
    on_train_epoch_start: Optional[List[Callable[[DetectionTrainer], None]]] = field(default_factory=list)
    on_train_epoch_end: Optional[List[Callable[[DetectionTrainer], None]]] = field(default_factory=list)
    on_train_end: Optional[List[Callable[[DetectionTrainer, object], None]]] = field(default_factory=list)

    def __post_init__(self):
        # None callbacks with empty list
        for f in fields(self):
            val = getattr(self, f.name)
            if val is None:
                setattr(self, f.name, [])

    def fire(self, name: str, *args, **kwargs):
        for cb in getattr(self, name):
            cb(*args, **kwargs)


@dataclass
class TrainingResults:
    metrics: list[dict]
    classes: list[str]
    trainer: DetectionTrainer

class YoloModelTrainer:
    @classmethod
    def train(
        cls,
        model: YOLO,
        dataset: YoloDataset,
        config: TrainingConfig,
        callbacks: TrainingCallbacks
    ):

        num_train_imgs = DatasetReader(dataset).count_images(split="train")
        batches_per_epoch = math.ceil(num_train_imgs / config.batch)
        total_batches = batches_per_epoch * config.epochs
        progress = TrainingProgress(
            batches_per_epoch,
            total_batches,
            config.epochs
        )

        model.reset_callbacks()
        for field in fields(callbacks):
            if field.name == "on_train_end":
                # wird später manuell aufgerufen
                continue
            func_list = getattr(callbacks, field.name)
            # total batches für progress hinzufügen
            if field.name == "on_train_batch_end":
                func_list = [cls._wrap_batch_end(func, progress) for func in func_list]

            for func in func_list:
                model.add_callback(field.name, func)

        # 
        model_info = YoloModelInspector.inspect(model)
        yolo_results = model.train(
                data=dataset.yaml_path,
                imgsz=config.imgsz,
                batch=config.batch,
                epochs=config.epochs,
                lr0=config.lr0,
                freeze= min(config.freeze, model_info.max_freeze),
                optimizer = config.optimizer,
                weight_decay = config.weight_decay,
                project=YoloModelStorage.TRAINING_PROJECT,
                name=YoloModelStorage.TRAINING_NAME,
                save_dir=(YoloModelStorage.TRAINING_PROJECT/YoloModelStorage.TRAINING_NAME).resolve(),
                verbose=False,
                exist_ok =True, 
                plots=False,
                seed=YoloModelStorage.TRAIN_SEED,
                resume=config.resume_training
            )

        # Datenaufbereitung
        class_results = yolo_results.to_df().rows(named=True)
        aggregate = {
            "Class": "Gesamt",
            "Images": num_train_imgs,
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

        metrics = TrainingResults( 
            metrics=full_results,
            classes=model.names,
            trainer=model.trainer
        )
        callbacks.fire("on_train_end", metrics)
        return metrics
    
 
    
    @staticmethod
    def _coco_to_xyxy(bbox:list):
        x, y, w, h = bbox
        return [x, y, x + w, y + h]

    
    @staticmethod
    def _wrap_batch_end(callback, progress:TrainingProgress):
        def wrapper(trainer:DetectionTrainer):
            if progress.epoch != trainer.epoch:
                progress.batch_count = 0
            progress.batch_count += 1
            progress.epoch = trainer.epoch
            callback(trainer, progress)  
        return wrapper