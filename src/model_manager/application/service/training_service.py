from typing import Optional, Callable, List
import logging
from ultralytics.models.yolo.detect import DetectionTrainer
from model_manager.repository.dataset_loader import YoloDatasetLoader
from model_manager.domain.services.dataset_validator import YoloDatasetValidator
from model_manager.domain.services.model_trainer import YoloModelTrainer, TrainingResults, TrainingCallbacks, TrainingConfig, TrainingProgress
from model_manager.repository.model_loader import YoloModelLoader, LoaderConfig
from model_manager.domain.services.model_inspector import YoloModelInspector, YoloModelInfo
from model_manager.domain.services.model_storage import YoloModelStorage


logger = logging.getLogger(__name__)

class YoloTrainingService():
    def __init__(self,
            dataset_path: str,
            model_name: str, 
            model_size: str, 
            pretrained: bool, 
            apply_transfer_learning: bool,
            freeze: int, 
            imgsz: int,
            batch: int,
            epochs: int,
            optimizer: str,
            lr0: float,
            weight_decay: float,
            weights_path: str | None = None, 
            resume_training:bool = False,
            on_train_start: Optional[List[Callable[[DetectionTrainer], None]]] = None,
            on_train_batch_start: Optional[List[Callable[[DetectionTrainer], None]]] = None,
            on_train_batch_end: Optional[List[Callable[[DetectionTrainer], None]]] = None,
            on_train_epoch_start: Optional[List[Callable[[DetectionTrainer], None]]] = None,
            on_train_epoch_end: Optional[List[Callable[[DetectionTrainer], None]]] = None,
            on_train_end: Optional[List[Callable[[DetectionTrainer, object], None]]] = None,
            on_error: Optional[List[Callable[[str], None]]] = None
        ):
        self.model_name = model_name
        self.model_size = model_size
        self.dataset_path = dataset_path
        self.batch = batch
        self.epochs = epochs
        self.optimizer = optimizer
        self.lr0 = lr0
        self.weight_decay = weight_decay
        self.weights_path =  weights_path 
        self.imgsz = imgsz

        self._cancel = False
        on_train_batch_start = [self._abort_if_cancelled] + (on_train_batch_start or [])
        self.train_callbacks = TrainingCallbacks(
            on_train_start , on_train_batch_start, on_train_batch_end, on_train_epoch_start,on_train_epoch_end,on_train_end
        )
        self.callbacks = {
            "on_error": on_error or []
        }    
        self.current_batch = 0
        self.batches_per_epoch = 0

        freeze = freeze if apply_transfer_learning else 0
        self.train_config = TrainingConfig(imgsz, batch, epochs, lr0, freeze, optimizer, weight_decay, resume_training)
       
        self.loader_config = LoaderConfig(model_name, model_size, pretrained, weights_path)
        if resume_training:
            if not weights_path:
                weights_path = YoloModelStorage.last_trained_model_path()
            self.loader_config.model_path = weights_path
        self.resume = resume_training



    def start_training(self) -> TrainingResults:
        logger.info("Starte Training")

        # Datensatz laden und validieren
        try:
            dataset = YoloDatasetLoader.load(self.dataset_path)
            dataset_validator = YoloDatasetValidator(dataset)
            dataset_validator.validate(split="train")
            dataset_validator.validate(split="val")
        except Exception as e:
            logger.exception(e)
            self._run_callbacks("on_error", f"Ungültiger Datensatz!\n{e}")
            return

        # Modell laden
        try:
            model = YoloModelLoader.load(self.loader_config)
        except Exception as e:
            logger.exception(e)
            self._run_callbacks("on_error", f"Modell konnte nicht geladen werden!\n\n{e}")
            return
    
        try:
            results = YoloModelTrainer.train(
                model, dataset, self.train_config, self.train_callbacks
            )
        except StopIteration as e:
            logger.info("Training abgebrochen")
            self._run_callbacks("on_error", f"Training wurde abgebrochen!")
            return
        except Exception as e:
            logger.exception(e)
            self._run_callbacks("on_error", f"Fehler beim Trainieren!\n\n{e}")
            return

        return results



    def _abort_if_cancelled(self, *args, **kwargs):
        if self._cancel:
            raise StopIteration
        
    def cancel(self):
        self._cancel = True
    
    def _run_callbacks(self, event, *arg):
        for func in self.callbacks[event]:
            func(*arg)


class YoloResultsAnalyzer:
    def __init__(self, results: TrainingResults):
        self.results = results
    
    def get_model_info(self) -> YoloModelInfo:
        model = self.results.trainer.model
        model_info = YoloModelInspector.inspect(model)
        return model_info
