from dataclasses import dataclass
from pathlib import Path
from model_manager.domain.models.dataset import YoloDataset
from model_manager.repository.dataset_reader import DatasetReader

class YoloDatasetValidator:
    """
    Validiert die Struktur und den Inhalt eines YOLO-Datensatzes.
    """

    VALID_SPLITS = {"train", "val", "test", "all"}

    def __init__(self, dataset:YoloDataset):
        self.dataset = dataset
        self.reader = DatasetReader(dataset)

    # -------------------------------------------------------
    # Public API
    # -------------------------------------------------------
    def validate(self, split: str = "all") -> bool:
        """
        Validiert einen oder alle Splits des Datensatzes.

        Args:
            split (str): "train", "val", "test" oder "all"

        Returns:
            bool: True wenn valide

        Raises:
            ValueError: bei ungültiger Struktur oder fehlenden Dateien
        """
        self._validate_yaml(self.reader.load_info())
        if split not in self.VALID_SPLITS:
            raise ValueError(
                f"Ungültiger Split '{split}'. "
                f"Erlaubt: {sorted(self.VALID_SPLITS)}"
            )

        if split == "all":
            for s in ("train", "val", "test"):
                self._validate_split(s)
        else:
            self._validate_split(split)

        return True

    # -------------------------------------------------------
    # Internal helpers
    # -------------------------------------------------------
    def _validate_split(self, split: str):
        img_folder: Path | None = getattr(self.dataset, f"{split}_images")
        lbl_folder: Path | None = getattr(self.dataset, f"{split}_labels")

        if img_folder is None:
            raise ValueError(f"Split '{split}' hat keinen Image-Pfad")

        if lbl_folder is None:
            raise ValueError(f"Split '{split}' hat keinen Label-Pfad")

        if not img_folder.exists():
            raise ValueError(
                f"Images-Ordner für Split '{split}' existiert nicht:\n{img_folder}"
            )

        if not lbl_folder.exists():
            raise ValueError(
                f"Labels-Ordner für Split '{split}' existiert nicht:\n{lbl_folder}"
            )

        images = list(self.reader.iter_files(split=split, file_type="images"))
        if not images:
            raise ValueError(
                f"Keine Bilder im Split '{split}' gefunden:\n{img_folder}"
            )

        labels = list(self.reader.iter_files(split=split, file_type="labels"))
        if not labels:
            raise ValueError(
                f"Keine Labels im Split '{split}' gefunden:\n{lbl_folder}"
            )

    def _validate_yaml(self, info: dict):
        if not isinstance(info, dict):
            raise ValueError("YAML Datei ist ungültig oder leer")
        
        if "names" not in info and "nc" not in info:
            raise ValueError("YAML Datei muss 'names' oder 'nc' enthalten")

        # if "names" not in info:
        #     raise ValueError("YAML Datei: 'names' fehlt")

        class_names = []
        if "names" in info:
            names = info["names"]
            if isinstance(names, dict):
                class_names = list(names.values())
            elif isinstance(names, list):
                class_names = names
            else:
                raise ValueError("YAML Datei: 'names' muss list oder dict sein")

            if not class_names:
                raise ValueError("YAML Datei: 'names' darf nicht leer sein")

        if "nc" in info:
            nc = info["nc"]
            if not isinstance(nc, int) or nc <= 0:
                raise ValueError(f"YAML Datei: 'nc' muss eine positive Zahl sein, aber ist {nc}")

            # Wenn names auch existieren, müssen nc und Anzahl Klassen übereinstimmen
            if class_names and nc != len(class_names):
                raise ValueError(
                    f"YAML Datei: 'nc' ({nc}) stimmt nicht mit Anzahl Klassen ({len(class_names)}) überein"
                )

        # names = info["names"]

        # if isinstance(names, dict):
        #     class_names = list(names.values())
        # elif isinstance(names, list):
        #     class_names = names
        # else:
        #     raise ValueError("YAML Datei: 'names' muss list oder dict sein")

        # if not class_names:
        #     raise ValueError("YAML Datei: 'names' darf nicht leer sein")

        # if "nc" not in info:
        #     raise ValueError("YAML Datei: 'nc' fehlt")

        

        # if info.get("nc") and info["nc"] != len(class_names):
        #     raise ValueError(
        #         f"YAML Datei: 'nc' ({info['nc']}) stimmt nicht mit Anzahl Klassen ({len(class_names)}) überein"
        #     )
