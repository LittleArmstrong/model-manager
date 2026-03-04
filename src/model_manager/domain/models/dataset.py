from dataclasses import dataclass
from pathlib import Path


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


    def get_label_path_from_image(self, img_path: Path):
        parts = img_path.relative_to(self.root).parts
        idx = None
        try:
            idx = parts.index("images")
            parts[idx] = "labels"
        except Exception as e:
            pass
        return self.root / Path(*parts).with_suffix(".txt")
    
    def get_path(self, split: str, type: str) -> Path|None:
        """
        Gibt den Pfad für Images oder Labels eines bestimmten Dataset-Splits zurück.

        Diese Methode erlaubt den generischen Zugriff auf Dataset-Pfade wie
        ``train_images``, ``val_labels`` usw., basierend auf Split und Typ.

        Args:
            split (str): Dataset-Split, z. B. ``"train"``, ``"val"`` oder ``"test"``.
            type (str): Pfadtyp, entweder ``"images"`` oder ``"labels"``.

        Returns:
            Path: Der angeforderte Pfad.

        Examples:
            >>> dataset.get_path("train", "images")
            PosixPath(".../images/train")

            >>> dataset.get_path("val", "labels")
            PosixPath(".../labels/val")
        """
        return getattr(self, f"{split}_{type}")



