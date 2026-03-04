from model_manager.repository.dataset_loader import YoloDataset
from model_manager.repository.dataset_reader import DatasetReader
from model_manager.repository.dataset_writer import DatasetWriter
import albumentations as A
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Callable
import logging

logger = logging.getLogger(__name__)

@dataclass(frozen=True)
class AugmentorConfig:
    num_augments: int
    rotation: int 
    translation: float 
    scale: float
    noise: float 
    brightness: float 
    contrast: float 
    flip_h: float 
    flip_v: float 

@dataclass(frozen=True)
class AugmentorResults:
    total_imgs: int
    total_aug_imgs: int
    success: int
    error: int


@dataclass(frozen=True)
class AugmentorCallbacks:
    on_progress: Optional[Callable[[int, int], None]] = None
    on_error:  Optional[Callable[[str], None]] = None
    on_done:  Optional[Callable[[AugmentorResults], None]] = None
    on_cancel: Optional[Callable[[AugmentorResults], None]] = None

class DatasetAugmentor:
    def __init__(self, config:AugmentorConfig, transform:A.Compose, reader:DatasetReader, writer: DatasetWriter, callbacks: AugmentorCallbacks = None):
        self.config = config
        self.transform = transform
        self.reader = reader
        self.writer = writer

        callbacks = callbacks if callbacks else AugmentorCallbacks()
        self.callbacks = {
            "on_progress": callbacks.on_progress,
            "on_done": callbacks.on_done,
            "on_error": callbacks.on_error,
            "on_cancel": callbacks.on_cancel
        }

    def augment(self) -> AugmentorResults:
        total_img_count = self.reader.count_images("train")
        total_aug_img_count = total_img_count * self.config.num_augments
        img_count = 0
        total_success_count = 0
        total_error_count = 0
        for image, img_path in self.reader.iter_files("train", "images", True):
            img_count += 1
            boxes, classes = self.reader.load_label_from_img(img_path)

            img_error_count = 0
            for i in range(self.config.num_augments):
                self._fire_cb("on_cancel")
                try:
                    aug_img = self.transform(
                        image=image,
                        bboxes=boxes,
                        class_labels=classes
                    )
                    total_success_count += 1
                except:
                    img_error_count += 1
                    total_error_count += 1
                    self._fire_cb("on_error", f"Fehler: {img_path.name} - {img_error_count} / {self.config.num_augments}" )
                    logger.debug(f"{img_path.name} konnte nicht augmentiert werden.")
                    continue

                # Speichern
                new_name = f"{img_path.stem}_aug_{i}"
                img_name = img_path.with_stem(new_name).name
                lbl_name = img_path.with_stem(new_name).with_suffix(".txt").name
                
                self.writer.save_image("train", img_name, aug_img["image"])
                self.writer.save_label("train", lbl_name, aug_img["bboxes"], aug_img["class_labels"])
            self._fire_cb("on_progress", img_count, total_img_count)
        results = AugmentorResults(total_img_count, total_aug_img_count, total_success_count, total_error_count)

        data_yaml = self.reader.load_info()
        param_dict = self._get_param_dict()
        if "augmentation" in data_yaml and isinstance(data_yaml["augmentation"], list):
            data_yaml["augmentation"].append(param_dict)
        else:
            data_yaml["augmentation"] = [param_dict]
        self.writer.save_yaml(data_yaml)

        self._fire_cb("on_done", results)
        return results
        
    
    def _fire_cb(self, cb, *args):
        if not self.callbacks[cb]:
            return
        self.callbacks[cb](*args)

    def _get_param_dict(self) -> dict:
        """Erstellt ein Dictionary der Augmentations-Hyperparameter aus Config."""
        return {
            "rotation": self.config.rotation,
            "translation": self.config.translation,
            "scale": self.config.scale,
            "noise": self.config.noise,
            "brightness": self.config.brightness,
            "contrast": self.config.contrast,
            "flip_h": self.config.flip_h,
            "flip_v": self.config.flip_v,
            "num_augments": self.config.num_augments
        }