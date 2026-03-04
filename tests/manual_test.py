import pytest
from pathlib import Path
import numpy as np
import cv2
import yaml
import random
import string

from model_manager.repository.dataset_reader import DatasetReader
from model_manager.domain.models.dataset import YoloDataset


def fake_dataset(tmp_path: Path) -> YoloDataset:
    dataset_dir = tmp_path / "dataset"
    images_dir = dataset_dir / "images"
    labels_dir = dataset_dir / "labels"

    splits = ["train", "val", "test"]

    # --- Ordner anlegen ---
    for split in splits:
        (images_dir / split).mkdir(parents=True)
        (labels_dir / split).mkdir(parents=True)

    # --- Helper: zufälliger Dateiname ---
    def random_name(ext: str) -> str:
        return "".join(random.choices(string.ascii_lowercase, k=8)) + ext

    # --- Daten erzeugen ---
    for split in splits:
        img_folder = images_dir / split
        lbl_folder = labels_dir / split

        # 2 gültige Bilder + Labels
        for i in range(2):
            img_path = img_folder / f"img_{i}.jpg"
            dummy_img = np.random.randint(
                0, 255, size=(10, 10, 3), dtype=np.uint8
            )
            cv2.imwrite(str(img_path), dummy_img)

            label_path = lbl_folder / f"img_{i}.txt"
            label_path.write_text("0 0.5 0.5 0.2 0.2\n")

        # --- Müll-Dateien (sollten ignoriert werden) ---
        (img_folder / random_name(".tmp")).write_text("junk")
        (img_folder / random_name(".json")).write_text("{}")
        (lbl_folder / random_name(".bak")).write_text("backup")
        (lbl_folder / random_name(".md")).write_text("# not a label")

    # Dummy YAML
    yaml_file = dataset_dir / "data.yaml"
    yaml_file.write_text(yaml.dump({"nc":2, "classes": ["cat", "dog"], "test": 'images/test', "train": "images/train", "val": "images/val"}))


    return YoloDataset(
        root=dataset_dir,
        train_images=images_dir / "train",
        train_labels=labels_dir / "train",
        val_images=images_dir / "val",
        val_labels=labels_dir / "val",
        test_images=images_dir / "test",
        test_labels=labels_dir / "test",
        yaml_path=yaml_file,
        num_classes="2",
        class_names=["cat", "dog"]
    )

if __name__ == "__main__":
    fake_dataset(Path("tests/tmp"))