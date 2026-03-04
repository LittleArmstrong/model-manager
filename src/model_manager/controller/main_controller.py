import os
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
import logging
from pathlib import Path

from model_manager.ui.view.window_main import MainWindow
from model_manager.controller.testing_controller import TestingController
from model_manager.controller.export_controller import ExportController
from model_manager.controller.training_controller import TrainingController, TrainingResults
from model_manager.controller.preprocessing_controller import PreprocessingController
from model_manager.controller.app_state import AppStateUI
from model_manager.application.service.model_exporter_service import YoloModelExporterService
from model_manager.application.service.code_exporter_service import CodeExporterService
from model_manager.application.service.info_service import InfoService
from model_manager.core.utils import resource_path


logger = logging.getLogger(__name__)

class MainController():
    training_done = qtc.Signal(object) 

    def __init__(self):
        self.app_state_ui = AppStateUI()
        self.view = MainWindow()
        self.view.setWindowIcon(qtg.QIcon(str(resource_path("logo.ico", internal=True))))
        self.view.showMaximized()

        self.view.btn_select_dataset.clicked.connect(self.select_dataset)
        # self.view.btn_save_model.clicked.connect(self.on_save_model_clicked)
        # self.view.btn_export_code.clicked.connect(self.on_code_export_clicked)

        self.training_controller = TrainingController(self.view.tab_training, self.app_state_ui)
        self.testing_controller = TestingController(self.view.tab_test, self.app_state_ui)
        self.preprocessing_controller = PreprocessingController(self.view.tab_preprocessing, self.app_state_ui)
        self.export_controller = ExportController(self.view.tab_export, self.app_state_ui)

        self.training_controller.training_end.connect(
            self._on_training_end
        )

        # testen
        if not InfoService.IS_FROZEN:
            folder_path = r"C:\Users\Baris\Projects\model_manager\data\coco8_custom"
            # folder_path = r"C:\Users\Baris\Projects\model_manager\data\strawberry"
            self.app_state_ui.dataset_path = folder_path
            self.view.set_dataset_path(folder_path) 

    @qtc.Slot()
    def select_dataset(self):
        folder_path = qtw.QFileDialog.getExistingDirectory(self.view, "Datensatz auswählen")
        if not folder_path:
            return
        logger.info("Datensatz ausgewählt")
        self.app_state_ui.dataset_path = folder_path
        # dataset_name = os.path.basename(folder_path)
        self.view.set_dataset_path(folder_path) 
    
    # @qtc.Slot()
    # def on_save_model_clicked(self):
    #     file_formats = {
    #         "YOLO PyTorch (*.pt)": None,
    #         "ONNX (*.onnx)": "onnx"
    #     }
    #     file_path, selected_filter = qtw.QFileDialog.getSaveFileName(
    #         self.view,
    #         "Modell speichern",
    #         str(Path.home()),
    #         "YOLO PyTorch (*.pt);;ONNX (*.onnx)"
    #     )

    #     if not file_path:
    #         return  # User hat abgebrochen
    #     try:
    #         YoloModelExporterService.export(Path(file_path), file_formats[selected_filter])
    #     except Exception as e:
    #         logger.exception(f"Fehler beim Modell Export: {e}")
    #         self.view.show_error_message(f"Fehler beim Modell Export:\n{e}")

    # @qtc.Slot()
    # def on_code_export_clicked(self):
    #     folder_path = qtw.QFileDialog.getExistingDirectory(self.view, "Ordner auswählen")
    #     if not folder_path:
    #         return
    #     try:
    #         CodeExporterService.export(folder_path)
    #     except Exception as e:
    #         logger.exception(f"Fehler beim Code Export: {e}")
    #         self.view.show_error_message(f"Fehler beim Code Export:\n{e}")  


    
    @qtc.Slot(object)
    def _on_training_end(self, results:TrainingResults):
        if not results:
            return
        model_name = self.training_controller.training_service.model_name
        model_size = self.training_controller.training_service.model_size
        self.testing_controller.on_new_trained_model(model_name, model_size)