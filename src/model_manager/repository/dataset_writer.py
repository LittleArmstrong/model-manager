from pathlib import Path
import shutil
import cv2
import numpy as np
import yaml
from PIL import Image
from typing import Iterable, List, Optional, Callable
from sklearn.model_selection import train_test_split
from model_manager.repository.dataset_loader import YoloDataset, RawDataset, YoloDatasetLoader
from dataclasses import dataclass
import math

class DatasetWriter:
    """
    Schreibt, kopiert oder exportiert einen bestehenden Datensatz.
    """
    def __init__(self, dataset: YoloDataset):
        """
        Args:
            dataset (YoloDataset): Der Quelldatensatz
        """
        self.dataset = dataset

    def copy_dataset(self, dst_dir: str | Path, loader: YoloDatasetLoader|None=None) -> Path:
        """
        Kopiert den gesamten Datensatz in einen neuen Ordner
        und gibt den neuen Pfad zurück.

        Args:
            dst_dir (str | Path): Zielverzeichnis

        Returns:
            path (Path | Dataset): Pfad zum kopierten Datensatz oder Dataset, wenn loader gegeben
        """
        dst = Path(dst_dir).resolve()

        if dst.exists():
            raise FileExistsError(f"Zielordner '{dst}' existiert bereits!")
        
        dst = shutil.copytree(self.dataset.root, dst)

        if loader:
            ds = loader.load(dst)
            return DatasetWriter(ds)
        return dst
    
    def save_image(self, split: str, name: str, img: np.ndarray) -> Path:
        """
        Speichert ein Bild im jeweiligen Split-Verzeichnis.
        
        Args:
            split (str): "train", "val", "test"
            name (str): Bildname
            img (np.ndarray): Bildinhalt
        
        Returns:
            path (Path): saved image path

        Raises:
            ValueError: falls split nicht existiert
        """
        # base = getattr(self.dataset, f"{split}_images")
        # if base is None:
        #     raise ValueError(f"Split '{split}' existiert nicht")
        base = self._get_split_path(split, "images")
        path = base / name
        ok = cv2.imwrite(str(path), cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
        if not ok:
            raise IOError(f"Bild konnte nicht gespeichert werden: {path}")

        return path

    def save_label(self, split: str, name: str, boxes: list[list[float]], classes: list[int]) -> Path:
        """
        Speichert ein Label im jeweiligen Split-Verzeichnis.
        
        Args:
            split (str): "train", "val", "test"
            name (str): Labelname
            boxes (list[list[float]]): Liste von Box-Werten im coco Format xywh
            classes (list[int]): Die Klassen zu den entpsprechenden Box-Werten
        
        Returns:
            path (Path | None): saved label path
        
        Raises:
            ValueError: falls split nicht existiert
        """
        # base = getattr(self.dataset, f"{split}_labels")
        # if base is None:
        #     raise ValueError(f"Split '{split}' existiert nicht")
        base = self._get_split_path(split, "labels")
        path = base / name
        with path.open("w") as f:
            for cls, (x, y, w, h) in zip(classes, boxes):
                f.write(f"{int(cls)} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n")
        return path


    def save_yaml(self, data: dict):
        """
        Überschreibt vollständig die bestehende Dataset-YAML-Datei

        Args:
            data (dict): Schlüssel/Werte, die eingefügt oder überschrieben werden sollen.
        """
        self.dataset.yaml_path.write_text(
            yaml.safe_dump(
                data,
                sort_keys=False,
                allow_unicode=True,
            ),
            encoding="utf-8-sig",
        )

    def _get_split_path(self, split: str, kind: str) -> Path:
        base = getattr(self.dataset, f"{split}_{kind}")
        if base is None:
            raise ValueError(f"Split '{split}' does not exist")
        return base
    

@dataclass(frozen=True)
class NewDatasetConfig:
    out_dir: Path
    pairs: list[tuple[Path, Path]]
    class_names: list[str]
    imgsz: int = 640
    train_size: float = 0.0
    val_size: float = 0.0
    test_size: float = 0.0

    def validate(self):
        total = self.train_size + self.val_size + self.test_size
        if not math.isclose(total, 1.0, abs_tol=1e-6):
            raise ValueError("Summe der Splits muss 1.0 ergeben!")
        
    



class RawDatasetWriter:
    def __init__(self, dataset: RawDataset):
        self.dataset = dataset

    def save_as_dataset(
        self,
        config: NewDatasetConfig,
        callback: Optional[Callable[[int], None]] = None,
        cancel: Optional[Callable[[int], None]] = None
    ):
        """
        Assumes validated split sizes.
        """
        out = Path(config.out_dir).resolve()
        out.mkdir()
        # -------------------------------------------------
        # Split
        # -------------------------------------------------
        train = [] 
        val = []
        test = []
        if config.train_size == 1.0:
            train = config.pairs
        elif config.val_size == 1.0:
            val = config.pairs
        elif config.test_size == 1.0:
            test = config.pairs
        else:
            train, temp = train_test_split(config.pairs, train_size=config.train_size, shuffle=True)
            if config.val_size == 0.0:
                test = temp
            elif config.test_size == 0.0:
                val = temp
            else:
                val, test = train_test_split(temp, test_size=config.test_size / (config.val_size + config.test_size), shuffle=True)
        splits = {"train": train, "val":val, "test":test}

        # -------------------------------------------------
        # Ordnerstruktur + Schreiben
        # -------------------------------------------------
        total = len(train) + len(val) + len(test)
        progress = 0
        for split, split_pairs in splits.items():
            img_split_folder = out / "images" / split
            lbl_split_folder = out / "labels" / split

            img_split_folder.mkdir(parents=True, exist_ok=True)
            lbl_split_folder.mkdir(parents=True, exist_ok=True)

            for img_path, lbl_path in split_pairs:
                img = Image.open(img_path).convert("RGB")
                img = img.resize((config.imgsz, config.imgsz))
                img.save(img_split_folder / img_path.name)

                shutil.copy(lbl_path, lbl_split_folder / lbl_path.name)
                progress += 1
                if callback:
                    callback(progress, total)
                if cancel:
                    cancel()

        data_yaml = {
            "train": f"images/train",
            "val": f"images/val",
            "test": f"images/test",
            "nc": len(config.class_names),
            "names": config.class_names,
            "split": {
                "train": config.train_size,
                "val": config.val_size,
                "test": config.test_size
            }
        }

        with open(out / "data.yaml", "w") as f:
            yaml.dump(data_yaml, f)



    # def __init__(
    #     self,
    #     output_root: Path,
    #     img_folder: str = "images",
    #     lbl_folder: str = "labels",
    #     img_size: int | None = None,
    # ):
    #     self.output_root = output_root
    #     self.img_folder = img_folder
    #     self.lbl_folder = lbl_folder
    #     self.img_size = img_size

    # def prepare_splits(self, splits: Iterable[str]):
    #     for split in splits:
    #         (self.output_root / self.img_folder / split).mkdir(parents=True, exist_ok=True)
    #         (self.output_root / self.lbl_folder / split).mkdir(parents=True, exist_ok=True)

    # def write_split(self, split: str, pairs: Iterable[tuple[Path, Path | None]]):
    #     for img_path, lbl_path in pairs:
    #         self._write_image(split, img_path)
    #         if lbl_path:
    #             self._write_label(split, lbl_path)

    # def _write_image(self, split: str, img_path: Path):
    #     out_path = (
    #         self.output_root
    #         / self.img_folder
    #         / split
    #         / img_path.name
    #     )

    #     img = Image.open(img_path).convert("RGB")
    #     if self.img_size:
    #         img = img.resize((self.img_size, self.img_size))

    #     img.save(out_path)

    # def _write_label(self, split: str, lbl_path: Path):
    #     out_path = (
    #         self.output_root
    #         / self.lbl_folder
    #         / split
    #         / lbl_path.name
    #     )
    #     shutil.copy(lbl_path, out_path)
