import sys
import os
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from model_manager.ui.designer.window_main_ui import Ui_MainWindow
from model_manager.ui.view.tab_training import TrainingTab
from model_manager.ui.view.tab_test import  TestTab
from model_manager.ui.view.tab_preprocessing import  PreprocessingTab
from model_manager.ui.view.tab_export import  ExportTab

class MainWindow(qtw.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.tab_training = TrainingTab()
        self.tab_test = TestTab()
        self.tab_preprocessing = PreprocessingTab()
        self.tab_export = ExportTab()
        
        self.setupUi(self)

        self.tabc_main.addTab(self.tab_preprocessing, "Preprocessing")
        self.tabc_main.addTab(self.tab_training, "Training")
        self.tabc_main.addTab(self.tab_test, "Test")
        self.tabc_main.addTab(self.tab_export, "Export")
    
    def set_dataset_path(self, path:str):
        self.lbl_selected_dataset.setText(path)

    def show_error_message(self, msg, title = "Fehler"):
        qtw.QMessageBox.critical(self, title, msg)