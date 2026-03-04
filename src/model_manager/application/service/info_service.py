from model_manager.domain.services.model_storage import YoloModelStorage
from model_manager.core.utils import is_frozen

class InfoService:
    YOLO_MODELS = YoloModelStorage.MODELS
    YOLO_MODEL_SIZES = YoloModelStorage.MODEL_SIZES
    YOLO_OPTIMIZERS = YoloModelStorage.OPTIMIZERS

    IS_FROZEN = is_frozen()

    TRAIN_SEED = YoloModelStorage.TRAIN_SEED
    
    @staticmethod
    def last_trained_model_path(best=True):
        path = YoloModelStorage.last_best_trained_model_path() if best else YoloModelStorage.last_trained_model_path()
        if path.exists():
            return path.resolve()
        
    @staticmethod
    def get_model_info(model:str):
        return YoloModelStorage.MODEL_INFO.get(model)