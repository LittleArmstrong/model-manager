from pathlib import Path
import cv2
import numpy as np
import albumentations as A
import yaml

from model_manager.repository.dataset_loader import YoloDatasetLoader
from model_manager.repository.dataset_reader import DatasetReader
from model_manager.domain.services.dataset_validator import YoloDatasetValidator
from model_manager.repository.dataset_writer import DatasetWriter


class ScalingService:
    def __init__(self, dataset_path:str, method:str="zscore"):
        self.dataset_path = dataset_path
        self.method = method

        self.dataset = None
        self.mean = [0,0,0]
        self.std = [0,0,0]

    def normalize(self):
        self.dataset = YoloDatasetLoader.load(self.dataset_path)
        YoloDatasetValidator.validate(self.dataset)
        self._calculate()
        self._save_config()


    # -------------------------------------------------------
    #  Load and validate dataset
    # -------------------------------------------------------

    # def _prepare_dataset(self):
    #     src_dataset = YoloDatasetLoader(self.dataset_path).load()
    #     YoloDatasetValidator(src_dataset).validate()
    #     dst_path = DatasetWriter.copy_dataset(src_dir=self.dataset_path, dst_dir = self.new_dataset_path)
    #     self.dataset = YoloDatasetLoader(dst_path).load()


    # -------------------------------------------------------
    # Compute mean & std on training images
    # -------------------------------------------------------

    def _calculate(self):
        if self.method == "zscore":
            self._compute_dataset_mean_std(minmax=False)
        elif self.method == "minmax+zscore":
            self._compute_dataset_mean_std(minmax=True)

    def _compute_dataset_mean_std(self, minmax=False):
        pixel_values_sum = np.zeros(3)
        pixel_values_sum_sq  = np.zeros(3)
        total_pixel_count = 0
 
        for img, _ in DatasetReader.load_images(self.dataset.train_images):
            img = img.astype(np.float32)

            h, w, _ = img.shape
            pixel_count_img = h * w
            pixel_values_img = img.reshape(-1, 3)
            if minmax:
                pixel_values_img /= 255.0

            pixel_values_sum += pixel_values_img.sum(axis=0)
            pixel_values_sum_sq += (pixel_values_img ** 2).sum(axis=0)

            total_pixel_count += pixel_count_img

        # druch 255 getei
        self.mean = (pixel_values_sum /  total_pixel_count) 
        self.std = (np.sqrt(pixel_values_sum_sq/total_pixel_count - self.mean ** 2)) 

        return self.mean, self.std
    

    # -------------------------------------------------------
    # Save configuration
    # -------------------------------------------------------

    def _save_config(self):
        config = DatasetReader.read_yaml(self.dataset.yaml_metadata_path)
        config.update({
            "mm_normalize": self.method,
            "mm_mean": self.mean.tolist() if isinstance(self.mean, np.ndarray) else self.mean,
            "mm_std": self.std.tolist() if isinstance(self.std, np.ndarray) else self.std,
        })
        DatasetWriter.save_yaml(self.dataset.yaml_metadata_path, data=config)


    # def _save_config(self):
    #     """
    #     Speichert die Methode und Werte im yaml
    #     """
    #     transform = A.Normalize(mean=self.mean .tolist(), std=self.std.tolist(), max_pixel_value=255.0, p=1.0)

    #     images = [self.dataset.train_images(), self.dataset.val_images(), self.dataset.test_images()]
    #     for img_generator in images:
    #         for img, img_path in img_generator:
    #             scaled = transform(image=img.astype(np.uint8))
    #             img_std = scaled['image']
    #             print(self.mean.tolist())
    #             print(self.std.tolist())
    #             print(img_std)

    #             DatasetWriter.save_image(img_std, img_path)


    # def _standardize_and_save_all(self):
    #     """
    #     Standardisiert ALLE split Bilder in input_dir (rekursiv) und speichert
    #     sie in output_dir mit gleicher Ordnerstruktur.
    #     """
    #     images = [self.dataset.train_images(), self.dataset.val_images(), self.dataset.test_images ()]
    #     for img_generator in images:
    #         for img, img_path in img_generator:
    #             # Bild laden
    #             img = img.astype(np.float32)

    #             # Standardisierung (Z-Score)
    #             img_std = (img - self.mean) / self.std

    #             # Optional: clip für Speicherung (visuell sinnvoll)
    #             img_std = np.clip(img_std, 0, 255).astype(np.uint8)

    #             DatasetWriter.save_image(img_std, img_path)

    