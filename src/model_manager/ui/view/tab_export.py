
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from dataclasses import dataclass
from pathlib import Path


from model_manager.ui.designer.tab_export_ui import Ui_ExportTab
import logging
logger = logging.getLogger(__name__)


class ExportTab(qtw.QWidget, Ui_ExportTab):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def show_error_message(self, msg, title = "Fehler"):
        qtw.QMessageBox.critical(self, title, msg)

    def set_model_path_best(self, path:Path|str):
        self.lbl_model_path.setText(str(path))

    def set_model_path_last(self, path:Path|str):
        self.lbl_model_path_last.setText(str(path))

    def allow_best_model_export_service(self, allow=True):
        self.btn_model_export.setDisabled(not allow)

    def allow_last_model_export_service(self, allow=True):
        self.btn_model_last_export.setDisabled(not allow)

    def set_train_seed(self, seed:str):
        self.lbl_train_seed.setText(seed)
    