
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
import logging
from dataclasses import dataclass

from model_manager.ui.designer.tab_preprocessing_ui import Ui_preprocessing_tab


logger = logging.getLogger(__name__)

@dataclass
class DatasetCreationConfigUI:
    train_split: float
    val_split: float
    test_split: float
    img_size: int
    class_names: list
    target_path: str
    name: str

@dataclass
class AugmentationConfigUI:
    name: str
    output_dir: str             
    aug_per_image: int 
    rotation: int = 15
    translation: float = 0.1
    scale: float = 0.2
    noise: float = 0.02
    brightness: float = 0.2
    contrast: float = 0.2
    flip_h: float = 0.5
    flip_v: float = 0.0

@dataclass
class ScalingConfigUI:
    method: str



class PreprocessingTab(qtw.QWidget, Ui_preprocessing_tab):
    create_dataset = qtc.Signal()
    augment_dataset = qtc.Signal()
    scale_dataset = qtc.Signal()
    choose_dataset_creation_path = qtc.Signal()
    choose_dataset_augment_path = qtc.Signal()
    load_dataset_preview = qtc.Signal()
    image_selected = qtc.Signal(qtc.QModelIndex)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_create_dataset.clicked.connect(self.create_dataset)
        self.btn_augment_dataset.clicked.connect(self.augment_dataset)
        self.btn_create_dataset_path.clicked.connect(self.choose_dataset_creation_path)
        self.btn_augment_dataset_path.clicked.connect(self.choose_dataset_augment_path)
        self.btn_load_dataset_preview.clicked.connect(self.load_dataset_preview)
        self.tv_dataset.clicked.connect(self.image_selected)
        
       
    # --- preview
    def set_image_tree_model(self, model:qtw.QFileSystemModel, path:str):
        self.tv_dataset.setModel(model)
        self.tv_dataset.setRootIndex(model.index(path))
        self.tv_dataset.setColumnHidden(1, True)  # Size
        self.tv_dataset.setColumnHidden(2, True)  # Type
        self.tv_dataset.setColumnHidden(3, True)  # Date Modified

    # --- augment
    def set_dataset_path_augment(self, value:str):
        self.le_augment_dataset_path.setText(value)
    
    def show_augment_progress(self, message:str):
        self.pte_augment_output.appendPlainText(message)

    def show_augment_progress_bar(self, value:int):
        self.pb_augment_progress.setValue(value)

    def get_dataset_augment_parameters(self):
        config = AugmentationConfigUI(
            name=self.le_augmented_dataset_name.text(),
            output_dir=self.le_augment_dataset_path.text(),
            aug_per_image=self.spin_num_per_img.value(),
            rotation=self.spin_rotation.value(),
            translation=self.dspin_translation.value(),
            scale=self.dspin_zoom.value(),
            noise=self.dspin_noise.value(),
            brightness=self.dspin_brightness.value(),
            contrast=self.dspin_contrast.value(),
            flip_h=self.dspin_flip_lr.value(),
            flip_v=self.dspin_flip_ud.value()
        )
        logger.debug(f"AugmenationConfig:\n{config}")
        return config
    
    def clear_augment_progress(self):
        self.pte_augment_output.clear()
        self.show_augment_progress_bar(0)

    def update_augment_button(self, running: bool):
        self.btn_augment_dataset.setText("Abbrechen" if running else "Datensatz augmentieren")
        self.btn_augment_dataset.setToolTip(
            "Bricht die Datensatzuaugmentierung ab."
            if running
            else "Augmentiert den ausgewählten Datensatz mit den gegebenen Parameter."
        )

    # --- create

    def get_dataset_creation_parameters(self):
        config = DatasetCreationConfigUI(
            train_split=self.spin_train_split.value(),
            val_split=self.spin_val_split.value(),
            test_split=self.spin_test_split.value(),
            img_size=self.spin_img_size.value(),
            class_names= self._parse_csv_string(self.le_class_names.text()),
            target_path=self.le_create_dataset_path.text(),
            name=self.le_dataset_name.text()
        )
        logger.debug(f"DatasetCreationConfig:\n{config}")
        return config
    

    def set_dataset_path_create(self, value:str):
        self.le_create_dataset_path.setText(value)

    def show_creation_progress_bar(self, value:int):
        self.pb_creation_progress.setValue(value)

    def update_create_button(self, running: bool):
        self.btn_create_dataset.setText("Abbrechen" if running else "Datensatz erstellen")
        self.btn_create_dataset.setToolTip(
            "Bricht die Datensatzerstellung ab."
            if running
            else "Erstellt einen neuen Datensatz aus dem gewählten Ordner mit den gegebenen Parameter."
        )

  
    # --- generic feedback
    def show_warning_message(self, msg, title = "Warnung"):
        qtw.QMessageBox.warning(None, title, msg)

    def show_info_message(self, msg, title = "Info"):
        qtw.QMessageBox.information(None, title, msg)
    
    
    # --- utils

    def _parse_csv_string(self, s: str):
        if not s.strip():
            return []
        return [item.strip() for item in s.split(",") if item.strip()]
    
    
