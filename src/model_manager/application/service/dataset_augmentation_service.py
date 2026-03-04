from pathlib import Path
import albumentations as A
import logging
from typing import Optional, Callable

from model_manager.repository.dataset_loader import YoloDatasetLoader
from model_manager.repository.dataset_reader import DatasetReader
from model_manager.domain.services.dataset_validator import YoloDatasetValidator
from model_manager.repository.dataset_writer import DatasetWriter
from model_manager.domain.services.dataset_augmentor import DatasetAugmentor, AugmentorCallbacks, AugmentorConfig, AugmentorResults

logger = logging.getLogger(__name__)

class AugmentationService:

    def __init__(self,
            source_dir: str,           
            output_dir: str,           
            dataset_name: str,
            aug_per_image: int = 3,
            rotation: int = 15,
            translation: float = 0.1,
            scale: float = 0.2,
            noise: float = 0.02,
            brightness: float = 0.2,
            contrast: float = 0.2,
            flip_h: float = 0.5,
            flip_v: float = 0.0,
            on_error: Optional[Callable[[str], None]] = None,
            on_progress: Optional[Callable[[int, int], None]] = None,
            on_done: Optional[Callable[[AugmentorResults], None]] = None,
        ):
        self._cancel = False
        self.src_dir = Path(source_dir)
        self.dst_dir = Path(output_dir) / dataset_name
        self.callbacks = {
            "on_error": on_error,
            "on_progress": on_progress,
            "on_done": on_done,
            "on_cancel": self._abort_if_cancelled
        }
        # Albumentations Pipeline
        self.transform = A.Compose(
            [
                # Rotation, Translation, Zoom
                A.Affine(
                    rotate=(-rotation, rotation),  # Grad
                    translate_percent={"x": (-translation, translation), "y": (-translation, translation)},  # rel. Verschiebung
                    scale=(1 - scale, 1 + scale),  # Zoom
                    keep_ratio= True,
                    p=1.0
                
                ),
                 # Horizontaler Flip
                A.HorizontalFlip(p=flip_h),

                # Vertikaler Flip
                A.VerticalFlip(p=flip_v),

                # Helligkeit & Kontrast
                A.RandomBrightnessContrast(
                    brightness_limit=brightness, 
                    contrast_limit=contrast,     
                    p=1.0 
                ),

                # Gaußsches Rauschen
                A.GaussNoise(
                    std_range= (0, noise),
                    p=1.0
                ),
            ],
            bbox_params=A.BboxParams(format="yolo", label_fields=["class_labels"])
        )
        self.config = AugmentorConfig(aug_per_image,rotation, translation, scale, noise, brightness, contrast, flip_h, flip_v )
        self.aug_callbacks = AugmentorCallbacks(on_progress, on_error, on_done, self._abort_if_cancelled)

    def augment_dataset(self) -> AugmentorResults:
        """Alle Bilder im train Ordner augmentieren."""
        src_dataset = YoloDatasetLoader.load(self.src_dir)
        YoloDatasetValidator(src_dataset).validate("train")
        reader = DatasetReader(src_dataset)
        writer = DatasetWriter(src_dataset).copy_dataset(self.dst_dir, loader=YoloDatasetLoader)
        augmentor = DatasetAugmentor(self.config, self.transform, reader, writer, self.aug_callbacks)
        results = augmentor.augment()
        return results
    
    def _abort_if_cancelled(self, *args, **kwargs):
        if self._cancel:
            raise StopIteration
        
    def cancel(self):
        self._cancel = True

       

    