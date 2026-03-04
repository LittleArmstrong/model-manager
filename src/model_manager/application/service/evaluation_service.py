from pathlib import Path
from typing import Optional, Callable
import logging
from ultralytics import YOLO
from ultralytics.models.yolo.detect import DetectionValidator
from model_manager.repository.dataset_loader import YoloDatasetLoader
from model_manager.domain.services.dataset_validator import YoloDatasetValidator
from model_manager.domain.services.model_tester import YoloModelTester, EvalConfig, EvalCallbacks, EvalResult
from model_manager.domain.services.model_storage import YoloModelStorage
from model_manager.repository.model_loader import YoloModelLoader, LoaderConfig

logger = logging.getLogger(__name__)


class YoloEvaluationService():
    def __init__(self, 
                dataset_path, 
                model_name: str='', 
                model_size: str = '',
                use_last_model: bool=False, 
                model_weights_path: str='', 
                # image_size: int=640, 
                batch_size: int=16, 
                min_score: float=0.25, 
                min_nms_iou: float=0.7,
                on_val_start:Optional[list[Callable[[DetectionValidator], None]]]=None,
                on_val_batch_start:Optional[list[Callable[[DetectionValidator], None]]]=None,
                on_val_batch_end:Optional[list[Callable[[DetectionValidator], None]]]=None,
                on_val_end:Optional[list[Callable[[object, object, str], None]]]=None,
                on_error:Optional[list[Callable[[str], None]]]=None,

                ):
        self.cancel = False

        self.model_name = model_name
        self.model_size = model_size
        self.use_last_model = use_last_model
        on_val_batch_start = [self._abort_if_cancelled] + (on_val_batch_start or [])
        self.val_callbacks = EvalCallbacks(
            on_val_start , on_val_batch_start, on_val_batch_end, on_val_end
        )
        self.callbacks = {
            "on_error": on_error or []
        }    
        self.dataset_path = dataset_path
        self.eval_config =  EvalConfig(batch_size, min_score, min_nms_iou)
        model_path = YoloModelStorage.last_best_trained_model_path() if use_last_model else None
        weights_path = model_weights_path if not use_last_model else None
        # self.load_config = LoaderConfig(model_path=model_path)
        self.load_config = LoaderConfig(model_name, model_size, weights_path=weights_path, model_path=model_path)

        self.current_batch = 0
        self.total_batches = 0


    def start_testing(self) -> EvalResult:
        logger.debug("Test gestartet")

        # Datensatz laden und validieren
        try:
            dataset = YoloDatasetLoader.load(self.dataset_path)
            YoloDatasetValidator(dataset).validate(split="test")
        except Exception as e:
            logger.exception(e)
            self._run_callbacks("on_error", f"Ungültiger Datensatz!\n{e}")
            return

        try:
            model = YoloModelLoader.load(self.load_config)
        except FileNotFoundError as e:
            logger.exception(e)
            if self.use_last_model:
                self._run_callbacks("on_error", f"Modell konnte nicht geladen werden!\n\nBitte vorher Modell trainieren.")
            else:
                self._run_callbacks("on_error", f"Modell konnte nicht geladen werden!\n\n{e}")
            return
        except Exception as e:
            logger.exception(e)
            self._run_callbacks("on_error", f"Modell konnte nicht geladen werden!\n\n{e}")
            return
        
        # Modell testen
        try:
            results = YoloModelTester.test(model, dataset, self.eval_config, self.val_callbacks)
        except StopIteration as e:
            logger.info("Validation cancelled by user")
            self._run_callbacks("on_error", f"Test wurde abgebrochen!")
            return

        except KeyError as e:
            # Anzahl Klassen im Datensatz höher als im trainierten Modell
            logger.exception(e)
            self._run_callbacks("on_error",
                                f"Fehler beim Testen: Ungültige Klassen-ID ({e.args[0]}) gefunden\n\n"
                                "Das verwendete Modell oder die Label-Dateien passen nicht zum Datensatz.\n\n"
                                "Bitte stelle sicher, dass:\n"
                                "- das Modell mit diesem Datensatz trainiert wurde\n"
                                "- die Label-Dateien die gleichen Klassen wie in der Konfigurationsdatai (YAML) verwenden"
            )
            return
        except Exception as e:
            logger.exception(e)
            self._run_callbacks("on_error", f"Fehler beim Testen!\n{e}")
            return
        
        return results

    def cancel_test(self):
        self.cancel = True
    
    def _abort_if_cancelled(self, *args, **kwargs):
        if self.cancel:
            raise StopIteration


    def _run_callbacks(self, event, *arg):
        for func in self.callbacks[event]:
            func(*arg)

