from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from pathlib import Path
import logging

from ultralytics.models.yolo.detect import DetectionValidator
from polars import DataFrame

from model_manager.ui.view.tab_test import TestTab
from model_manager.controller.app_state import AppStateUI
from model_manager.application.service.evaluation_service import  YoloEvaluationService, EvalResult
from model_manager.application.service.predictions_service import  draw_predictions_on_image
from model_manager.controller.worker import Worker
from model_manager.controller.models import MetricsTableModel
from model_manager.application.service.info_service import InfoService
from model_manager.application.service.training_service import YoloModelInfo


logger = logging.getLogger(__name__)

class TestingController(qtc.QObject):
    val_start = qtc.Signal(object)
    batch_start = qtc.Signal(object)
    batch_end = qtc.Signal(object, int) 
    val_end = qtc.Signal(object)
    test_error = qtc.Signal(str)
    image_index_changed = qtc.Signal(int) 


    def __init__(self, view:TestTab, app_state_ui:AppStateUI):
        super().__init__()
        self.view = view
        self.app_state_ui = app_state_ui
        self.model_weights_path = ""
        self.testing_service = None 
        self.worker = None
        self.test_results = None

        self.results_model = MetricsTableModel()    
        self.view.set_table_results_model(self.results_model)
    
        self.image_index = 0

        self.view.set_models(InfoService.YOLO_MODELS, InfoService.YOLO_MODEL_SIZES)

        self.view.testing_started.connect(self._start_testing)
        self.view.import_weights_pushed.connect(self._select_model_weights_path)
        self.val_end.connect(self._on_val_end)
        self.batch_end.connect(self._on_batch_end)
        self.test_error.connect(self._on_test_error)

        self.view.next_image.connect(lambda: self.image_index_changed.emit(self.image_index + 1))
        self.view.previous_image.connect(lambda: self.image_index_changed.emit(self.image_index -1))
        self.image_index_changed.connect(self._on_img_index_changed)
        self.view.img_order_changed.connect(self._on_img_order_changed)
        self.view.use_last_model_toggled.connect(self._on_use_last_model_toggled)

    def on_new_trained_model(self, name:str, size:str):
        self.view.set_model(name, size)



    def _start_testing(self):
        if self.worker and self.worker.isRunning():
            logger.debug("Test läuft → Abbruch wird angefordert")
            self.testing_service.cancel_test()
            return
        
        logging.debug("Starte Test")

        if not self.app_state_ui.dataset_path:
            self.view.show_warning_message("Kein Datensatz ausgewählt!")
            self._on_test_finished()
            return
        
        self.view.update_test_button(running=True)
        self.test_results = None
        self.view.clear_output()
        self.results_model.clear()

        # get ui values
        parameters = self.view.get_test_parameters()

        if not parameters.use_last_model and not self.model_weights_path:
            self.view.show_warning_message("Keine Modellgewichte ausgewählt!")
            self._on_test_finished()
            return

        self.testing_service = YoloEvaluationService(
            self.app_state_ui.dataset_path,
            parameters.model_name,
            parameters.model_size,
            parameters.use_last_model,
            self.model_weights_path,
            parameters.batch_size,
            parameters.min_score / 100.0,
            parameters.min_nms_iou / 100.0,
            on_val_batch_end=[self.batch_end.emit],
            on_val_end=[self.val_end.emit],
            on_error=[self.test_error.emit],
        )

        self.worker = Worker(task=self.testing_service.start_testing)
        self.worker.finished.connect(self._on_test_finished)
        self.worker.error.connect(self._on_test_error)
        self.worker.start()


    @qtc.Slot()
    def _select_model_weights_path(self):
        file_path = qtw.QFileDialog.getOpenFileName(self.view, caption="Gewichte auswählen", filter="PyTorch-YOLO-Modell (*.pt)")[0]
        if not file_path:
            return
        self.model_weights_path = Path(file_path)
        self.view.set_model_weights_file_name(self.model_weights_path.name) 



    @qtc.Slot(object)
    def _on_val_end(self, results:EvalResult):
        self.test_results = results
        self._on_img_order_changed("Original")
        self.results_model.setRows(results.metrics)        
        self.image_index_changed.emit(0)

    @qtc.Slot(int)
    def _on_img_index_changed(self, new_index):
        if not self.test_results:
            return
        self.image_index = min( max(0, new_index), len(self.test_results.predictions) - 1)
        img_info = self.test_results.predictions[self.image_index]
        img = draw_predictions_on_image(prediction=img_info, image_folder=self.test_results.img_path, class_names=self.test_results.classes)
        self.view.show_image(img)


    @qtc.Slot(str)
    def _on_img_order_changed(self, new_order: str):
        """
        Sortiert die Predictions-Liste basierend auf dem gewählten Kriterium.

        Args:
            new_order (str): Sortieroption, z.B. "Original", "Score aufsteigend", "Score absteigend"
        """
        if not self.test_results:
            return

        sort_options = {
            "Original": {
                "key": lambda p: p.get("file_name", ""),
                "reverse": False,
            },
            "Score aufsteigend": {
                "key": lambda p: p.get("min_score", 0),
                "reverse": False,
            },
            "Score absteigend": {
                "key": lambda p: p.get("max_score", 0),
                "reverse": True,
            },
        }

        option = sort_options.get(new_order, sort_options["Original"])
        self.test_results.predictions.sort(
            key=option["key"],
            reverse=option["reverse"]
        )


        # Aktuelles Bild neu anzeigen
        self.image_index_changed.emit(0)

    @qtc.Slot(object, int)
    def _on_batch_end(self, validator:DetectionValidator,  total_batches:int):
        progress = int((validator.batch_i+1) / total_batches * 100)
        self.view.set_progress_bar(progress)

    @qtc.Slot(bool)
    def _on_use_last_model_toggled(self, checked: bool):
        self.view.set_import_weigths_state(checked) 
        self.view.set_model_state(checked) 

    @qtc.Slot(str)
    def _on_dataset_error(self, msg:str):
        self.view.show_error_message(msg)

    @qtc.Slot(str)
    def _on_model_error(self, msg:str):
        self.view.show_error_message(msg)

    @qtc.Slot(str)
    def _on_test_error(self, msg:str):
        self.view.show_error_message(msg)

    @qtc.Slot(str)
    def _on_test_finished(self, results:dict|None=None):
        self.view.update_test_button(running=False)

    @qtc.Slot(str)
    def on_test_canceled(self, msg:str):
        self.view.set_progress_bar(0)

    