from dataclasses import dataclass

@dataclass
class AppStateUI:
    dataset_path: str = ""
    import_model_path: str = ""
    