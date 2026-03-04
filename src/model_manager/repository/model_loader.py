from ultralytics import YOLO
from model_manager.domain.services.model_inspector import YoloModelInspector
from model_manager.domain.services.model_storage import YoloModelStorage
from dataclasses import dataclass
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

@dataclass
class LoaderConfig:
    model_name: str = ""
    model_size: str = ""
    use_pretrained: bool = False
    weights_path: Path|str | None = None
    model_path: Path | None = None

class YoloModelLoader:
    @staticmethod
    def load(config:LoaderConfig) -> YOLO:
        if config.model_path:
            if not config.model_path.exists():
                raise FileNotFoundError(f"Modell nicht gefunden: {config.model_path}")
            return YOLO(config.model_path)    
        model_path = YoloModelStorage.pretrained_model_path(config.model_name, config.model_size)
        model = YOLO(model_path)
        
        if config.use_pretrained:
            return model
        
        if not config.weights_path:
            model.reset_weights()
            return model
        
        weights_path = Path(config.weights_path).resolve()
        if not weights_path.exists():
            raise FileNotFoundError(f"Gewichte nicht gefunden: {config.weights_path}")
        
        weight_model = YOLO(weights_path)
        weight_model_info = YoloModelInspector.inspect(weight_model)
        if (weight_model_info.name != config.model_name.lower() or weight_model_info.size != config.model_size.lower()):
            raise ValueError(f"Modellgewichte '{weight_model_info.name}{weight_model_info.size}' passen nicht zur ausgewählten Architektur '{config.model_name}{config.model_size}'!")
        logger.debug(f"model: {config.model_name} {config.model_size} weights: {weight_model_info.name} {weight_model_info.size} {weights_path}")
        model.load(weights_path)
        return model

    @staticmethod
    def load_last_trained(best=True) -> YOLO:
        path = YoloModelStorage.last_best_trained_model_path() if best else YoloModelStorage.last_trained_model_path() 
        if not path.exists():
            raise FileNotFoundError(f"Modell nicht gefunden: {path}")
        return YOLO(path)

        
