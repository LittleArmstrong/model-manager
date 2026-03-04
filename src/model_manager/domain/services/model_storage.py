from pathlib import Path
from model_manager.core.utils import resource_path
from model_manager.domain.services.model_inspector import YoloModelInfo

class YoloModelStorage:
    PRETRAINED_BASE = resource_path("detection_models", internal=True)

    PROJECT_BASE = resource_path("runs", relative=True)
    TRAINING_PROJECT = PROJECT_BASE / "training"
    TRAINING_NAME = "qt01"
    TESTING_PROJECT = PROJECT_BASE / "testing"
    TESTING_NAME = "qt01"

    MODELS = ("YOLOv26","YOLOv12","YOLOv11", "YOLOv10")
    MODEL_SIZES = ("n", "s", "m", "l", "x")
    OPTIMIZERS = ("auto", "SGD", "Adam", "AdamW")

    MODEL_INFO ={
        "YOLOv26": YoloModelInfo("YOLOv26","-", 11,13,23),
        "YOLOv12": YoloModelInfo("YOLOv12","-", 9,13,21),
        "YOLOv11": YoloModelInfo("YOLOv11","-", 11,13,23),
        "YOLOv10": YoloModelInfo("YOLOv10","-", 11,13,23),
    }

    TRAIN_SEED = 7428321
    

    @classmethod
    def pretrained_model_path(cls, name: str, size: str) -> Path:
        return (cls.PRETRAINED_BASE / name / size).with_suffix(".pt")

    @classmethod
    def last_best_trained_model_path(cls) -> Path:
        """
        Get the path to the last trained model of the epoch with the best parameter
        """
        return cls.TRAINING_PROJECT / cls.TRAINING_NAME / "weights" / "best.pt"
    
    @classmethod
    def last_trained_model_path(cls) -> Path:
        """
        Get the path to the last trained model of the last epoch
        """
        return cls.TRAINING_PROJECT / cls.TRAINING_NAME / "weights" / "last.pt"