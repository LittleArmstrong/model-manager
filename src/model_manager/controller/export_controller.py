from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from pathlib import Path
import logging
from functools import partial

from model_manager.application.service.model_exporter_service import YoloModelExporterService
from model_manager.application.service.code_exporter_service import CodeExporterService
from model_manager.ui.view.tab_export import ExportTab
from model_manager.controller.app_state import AppStateUI
from model_manager.application.service.info_service import InfoService


logger = logging.getLogger(__name__)

class ExportController(qtc.QObject):
    def __init__(self, view:ExportTab, app_state_ui:AppStateUI):
        super().__init__()
        self.view = view
        self.app_state_ui = app_state_ui

        self.view.btn_model_export.clicked.connect(partial(self.on_save_model_clicked, True))
        self.view.btn_model_last_export.clicked.connect(partial(self.on_save_model_clicked, False))
        self.view.btn_code_export.clicked.connect(self.on_code_export_clicked)

        model_best_path = InfoService.last_trained_model_path(best=True)
        if model_best_path:
            self.view.set_model_path_best(model_best_path)
            self.view.allow_best_model_export_service(True)

        model_last_path = InfoService.last_trained_model_path(best=False)
        if model_last_path:
            self.view.set_model_path_last(model_last_path)
            self.view.allow_last_model_export_service(True)
        self.view.set_train_seed(str(InfoService.TRAIN_SEED))
            

    @qtc.Slot(bool)
    def on_save_model_clicked(self, best_model):
        file_formats = {
            "YOLO PyTorch (*.pt)": None,
            "ONNX (*.onnx)": "onnx"
        }
        file_path, selected_filter = qtw.QFileDialog.getSaveFileName(
            self.view,
            "Modell speichern",
            str(Path.home()),
            "YOLO PyTorch (*.pt);;ONNX (*.onnx)"
        )

        if not file_path:
            return  # User hat abgebrochen
        try:
            YoloModelExporterService.export(Path(file_path), file_formats[selected_filter], best_model)
        except Exception as e:
            logger.exception(f"Fehler beim Modell Export: {e}")
            self.view.show_error_message(f"Fehler beim Modell Export:\n{e}")

    @qtc.Slot()
    def on_code_export_clicked(self):
        folder_path = qtw.QFileDialog.getExistingDirectory(self.view, "Ordner auswählen")
        if not folder_path:
            return
        try:
            CodeExporterService.export(folder_path)
        except Exception as e:
            logger.exception(f"Fehler beim Code Export: {e}")
            self.view.show_error_message(f"Fehler beim Code Export:\n{e}")  

