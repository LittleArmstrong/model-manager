from pathlib import Path
import cv2
from typing import  Generator, Optional, Union, Tuple, List
import numpy as np
import yaml
from model_manager.core.config import LABEL_EXTENSIONS, IMAGE_EXTENSIONS
from model_manager.repository.dataset_loader import YoloDataset, RawDataset



class DatasetReader:
    def __init__(self, dataset:YoloDataset, ext:dict|None = None):
        self.dataset = dataset
        self.image_exts = ext["image_exts"] if ext and ext["image_exts"] else IMAGE_EXTENSIONS
        self.label_exts = ext["label_exts"] if ext and ext["label_exts"] else LABEL_EXTENSIONS

    # --- Zentrale File-Iteration ---
    def iter_files(
        self, 
        split: str, 
        file_type: str, 
        load: bool = False
    ) ->  Generator[
    Union[Path, Tuple[Optional[np.ndarray], Path], Tuple[List[List[float]], List[int], Path]], None, None
    ]:
        """
        Iteriert über die Files eines Splits.
        
        Args:
            split: "train", "val", "test"
            file_type: "images" oder "labels"
            load: ob Inhalte direkt geladen werden sollen
        
        Yields:
            images: Tuple[Optional[np.ndarray], Path] wenn file_type="images" und load=True
            labels: Tuple[List[float], List[int], Path] wenn file_type="labels" und load=True
            sonst Path
        """
        folder_map = {
            "train": {"images": self.dataset.train_images, "labels": self.dataset.train_labels},
            "val":   {"images": self.dataset.val_images,   "labels": self.dataset.val_labels},
            "test":  {"images": self.dataset.test_images,  "labels": self.dataset.test_labels},
        }
        ext_map = {"images": self.image_exts, "labels": self.label_exts}
        folder = folder_map[split][file_type]
        ext = ext_map[file_type]

        for path in folder.iterdir():
            if path.suffix.lower() not in ext:
                continue

            if load:
                if file_type == "images":
                    yield self.load_image(path), path
                elif file_type == "labels":
                    boxes, classes = self.load_label(path)
                    yield boxes, classes, path
            else:
                yield path
        

    @staticmethod
    def load_image(img_path: Path):
        img = cv2.imread(str(img_path))
        if img is None:
            return None
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img
    
    @staticmethod
    def load_label(label_path: Path):
        """YOLO labels einlesen."""
        boxes = []
        classes = []
        if not label_path.exists():
            return boxes, classes

        with label_path.open(encoding="utf-8-sig") as f:
            for line in f:
                cls, x, y, w, h = map(float, line.split())
                boxes.append([x, y, w, h])
                classes.append(int(cls))
        return boxes, classes

    def load_label_from_img(self, img_path: Path):
        parts = list(img_path.relative_to(self.dataset.root).parts)
        idx = None
        try:
            idx = parts.index("images")
            parts[idx] = "labels"
        except Exception as e:
            pass
        label_path = self.dataset.root / Path(*parts).with_suffix(".txt")
        return self.load_label(label_path)

    def count_images(self, split: str) -> int:
        return sum(1 for _ in self.iter_files(split, "images", load=False))

    
    def load_info(self):
        content = self.dataset.yaml_path.read_text(encoding="utf-8-sig")
        return yaml.safe_load(content)


class RawDatasetReader:
    def __init__(self, dataset:RawDataset, ext:dict|None = None):
        self.dataset = dataset
        self.image_exts = ext["image_exts"] if ext and ext.get("image_exts") else IMAGE_EXTENSIONS
        self.label_exts = ext["label_exts"] if ext and ext.get("label_exts") else LABEL_EXTENSIONS

    def iter_pairs(self):
        # Alle Label-Dateien sammeln: stem -> [Path, ...]
        label_map: dict[str, list[Path]] = {}

        for lbl_dir in self.dataset.label_dirs:
            for lbl in lbl_dir.iterdir():
                if lbl.is_file() and lbl.suffix.lower() in self.label_exts:
                    label_map.setdefault(lbl.stem, []).append(lbl)

        # Bilder iterieren
        for img_dir in self.dataset.image_dirs:
            for img in img_dir.iterdir():
                if not img.is_file() or img.suffix.lower() not in self.image_exts:
                    continue

                #  Direktes Label neben dem Bild
                direct_label = img.with_suffix(".txt")
                if direct_label.exists():
                    yield img, direct_label
                    continue
                
                # kein Label
                candidates = label_map.get(img.stem, [])
                if not candidates:
                    yield img, None  # kein Label → überspringen (oder später strict)
                    continue

                # Kandidaten mit gleichem Namen
                # hol label mit dem geringsten Unterschied im Pfad
                img_parts = img.relative_to(self.dataset.root).parts
                scored = []
                for lbl in candidates:
                    lbl_parts = lbl.relative_to(self.dataset.root).parts

                    # Distanz = Anzahl unterschiedlicher Parts
                    diff = sum(
                        1 for a, b in zip(img_parts, lbl_parts) if a != b
                    ) + abs(len(img_parts) - len(lbl_parts))

                    scored.append((diff, lbl))

                scored.sort(key=lambda x: x[0])
                best_diff = scored[0][0]
                best = [lbl for d, lbl in scored if d == best_diff]

                if len(best) > 1:
                    raise ValueError(
                        f"Mehrere Labels für Bild {img} gefunden: {best}"
                    )

                yield img, best[0]
    

    # def load(cls, path: Path) -> RawDataset:
    #     images = [p for p in path.rglob("*") if p.suffix.lower() in IMAGE_EXTENSIONS]
    #     labels = [p for p in path.rglob("*") if p.suffix.lower() in LABEL_EXTENSIONS]
    #     # pairs = [(path / "img1.png", path / "img1.txt"), (path / "img2.png", path / "img2.txt")]

    #     label_map = defaultdict(list)
    #     for lbl in labels:
    #         label_map[lbl.stem].append(lbl)

    #     # 3️⃣ Paare bilden
    #     pairs = []
    #     for img in images:
    #         preferred_label = None

    #         # a) gleiche Datei direkt daneben prüfen
    #         candidate = img.with_suffix(".txt")
    #         if candidate.exists():
    #             preferred_label = candidate
    #         else:
    #             # b) sonst irgendwo im Dataset nach Label mit gleichem Stem suchen
    #             candidates = label_map.get(img.stem, [])
    #             if candidates:
    #                 preferred_label = candidates[0]  # ersten nehmen, Reihenfolge durch sorted() vorher fixierbar

    #         if preferred_label:
    #             pairs.append((img, preferred_label))

    #     return RawDataset(images, labels, pairs)