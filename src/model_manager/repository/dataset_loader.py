from pathlib import Path
import yaml
import cv2
from typing import List, Generator, Optional
from collections import defaultdict
from dataclasses import dataclass
from model_manager.core.config import LABEL_EXTENSIONS, IMAGE_EXTENSIONS

@dataclass(frozen=True)
class YoloDataset:
    root: Path
    train_images: Path | None
    val_images: Path | None
    test_images: Path | None
    train_labels: Path | None
    val_labels: Path | None
    test_labels: Path | None
    class_names: tuple[str, ...]
    num_classes: int
    yaml_path: Path


class YoloDatasetLoader:
    @classmethod
    def load(cls, dataset_dir: str | Path) -> YoloDataset:
        root = Path(dataset_dir).resolve()
        if not root.exists():
            raise ValueError(f"Datensatz {root} existiert nicht!")
        
        # get yaml file
        # yaml_path = cls._get_yaml_file_path(root)
        data_yaml = root / "data.yaml"
        if data_yaml.exists():
            yaml_path = data_yaml
        else:
            yaml_files = list(root.glob("*.yaml"))
            if not yaml_files:
                raise FileNotFoundError("Keine YAML Datei gefunden.")
            if len(yaml_files) > 1:
                raise ValueError("Mehrere YAML Dateien gefunden. Erwartet genau eine oder 'data.yaml'.")
            yaml_path =  yaml_files[0]
        data = yaml.safe_load(yaml_path.read_text(encoding="utf-8-sig"))
        if not data:
            raise ValueError("YAML Datei leer.")

        # Required structure in YOLO YAML
        train = data.get("train")
        val = data.get("val")
        test = data.get("test")
        names = tuple( data.get("names", ()))
        num_classes = data.get("nc", len(names))

        # Paths
        train_img_path = root / cls._clean_path(train) if train else None
        val_img_path   = root / cls._clean_path(val) if val else None
        test_img_path  = root / cls._clean_path(test) if test else None

        image_folders = {"train": train_img_path, "val": val_img_path, "test": test_img_path}
        label_folders = {}
        for split, folder_path in image_folders.items():
            if not folder_path:
                label_folders[split] = None
                continue
            # ultralytics uses the yolo dataset which replaces images with labels for the label path
            # if it exists
            parts = list(folder_path.relative_to(root).parts)
            idx = None
            try:
                idx = parts.index("images")
                parts[idx] = "labels"
            except ValueError:
                pass

            label_folders[split] = root / Path(*parts)

        return YoloDataset(
            root=root,
            train_images=train_img_path,
            val_images=val_img_path,
            test_images=test_img_path,
            train_labels=label_folders["train"],
            val_labels=label_folders["val"],
            test_labels=label_folders["test"],
            class_names=names,
            num_classes=num_classes,
            yaml_path=yaml_path
        )
    
    @staticmethod
    def _clean_path(path: str) -> str:
        if path.startswith("./"):
            return path[2:]
        
        if path.startswith("../"):
            return path[3:]
        return path



@dataclass(frozen=True)
class RawDataset:
    root: Path
    image_dirs: tuple[Path]
    label_dirs: tuple[Path]


class RawDatasetLoader:
    @classmethod
    def load(cls, root: Path, ext: dict|None=None) -> RawDataset:
        if not root.exists():
            raise FileNotFoundError(f"Pfad {root} existiert nicht!")
        image_exts = ext["image_exts"] if ext and ext.get("image_exts") else IMAGE_EXTENSIONS
        label_exts = ext["label_exts"] if ext and ext.get("label_exts") else LABEL_EXTENSIONS

        image_dirs = set()
        label_dirs = set()

        for p in root.rglob("*"):
            if not p.is_file():
                continue

            if p.suffix.lower() in image_exts:
                image_dirs.add(p.parent)
            elif p.suffix.lower() in label_exts:
                label_dirs.add(p.parent)

        if not image_dirs:
            raise FileNotFoundError("Keine Bilder gefunden.")
        if not label_dirs:
            raise FileNotFoundError("Keine Labels gefunden.")

        return RawDataset(
            root=root,
            image_dirs=tuple(sorted(image_dirs)),
            label_dirs=tuple(sorted(label_dirs)),
        )
    
