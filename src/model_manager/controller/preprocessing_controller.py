from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from pathlib import Path
import logging
import textwrap


from model_manager.ui.view.tab_preprocessing import PreprocessingTab
from model_manager.controller.app_state import AppStateUI
from model_manager.controller.worker import Worker
from model_manager.application.service.dataset_creation_service import  DatasetCreationService
from model_manager.application.service.dataset_augmentation_service import AugmentationService, AugmentorResults
from model_manager.application.service.dataset_scaling_service import ScalingService


logger = logging.getLogger(__name__)


class PreprocessingController(qtc.QObject):
    augment_error = qtc.Signal(str) 
    augment_progress = qtc.Signal(int, int)
    augment_done = qtc.Signal(object)
    creation_done = qtc.Signal(object)
    creation_error = qtc.Signal(object)
    creation_progress = qtc.Signal(int, int)

    def __init__(self, view:PreprocessingTab, app_state_ui:AppStateUI):
        super().__init__()
        self.view = view
        self.app_state_ui = app_state_ui

        self.worker = 0
        self.augment_worker = None
        self.augment_service = None
        self.create_worker = None
        self.create_service = None
        self.preview_model = None

        # --- create
        self.view.create_dataset.connect(self._on_create_dataset)
        self.view.choose_dataset_creation_path.connect(self._on_select_dataset_creation_path)
        self.creation_done.connect(self._on_creation_done)
        self.creation_error.connect(self._on_creation_error)
        self.creation_progress.connect(self._on_creation_progress)

        # --- augment
        self.view.augment_dataset.connect(self._on_augment_dataset)
        self.view.choose_dataset_augment_path.connect(self._on_select_dataset_augment_path)
        self.augment_error.connect(self._on_augment_progress_error)
        self.augment_done.connect(self._on_augment_done)
        self.augment_progress.connect(self._on_augment_progress)
        
        # --- preview
        self.view.load_dataset_preview.connect(self._on_load_dataset_preview)
        self.view.image_selected.connect(self._on_image_selected)



    # --- preview

    @qtc.Slot()
    def _on_load_dataset_preview(self):
        model = qtw.QFileSystemModel()
        path = self.app_state_ui.dataset_path
        model.setRootPath(path)
        model.setNameFilters(["*.png", "*.jpg", "*.jpeg"])
        model.setNameFilterDisables(False)
        self.view.set_image_tree_model(model, path)
        self.preview_model = model

    @qtc.Slot(object)
    def _on_image_selected(self, index:qtc.QModelIndex):
        # Voller Pfad zur Datei
        model = self.preview_model
        file_path = model.filePath(index)

        # Prüfen, ob es eine Datei ist (kein Ordner)
        if not model.isDir(index):
            pixmap = qtg.QPixmap(file_path)
            self.view.lbl_img.setPixmap(pixmap)
            self.view.lbl_img.setScaledContents(True)  # Bild an Label anpassen
        

    #--- augment
    @qtc.Slot()
    def _on_augment_dataset(self):
        if self.augment_worker and self.augment_worker.isRunning():
            logger.debug("Augmentierung läuft → Abbruch wird angefordert")
            self.augment_service.cancel()
            self.view.show_warning_message("\nAugmentierung abgebrochen!")
            self.view.clear_augment_progress()
            self.view.show_augment_progress("Augmentierung abgebrochen!")
            self.view.update_augment_button(False)
            return
        if not self.app_state_ui.dataset_path:
            self.view.show_warning_message("Kein Datensatz ausgewählt!")
            return
        params = self.view.get_dataset_augment_parameters()
        if not params.output_dir:
            self.view.show_warning_message("Bitte Speicherort auswählen!")
            return
        logging.debug("Starte Augmentation")
        self.view.clear_augment_progress()
        self.view.update_augment_button(True)

  
        service = AugmentationService(
            source_dir=self.app_state_ui.dataset_path,
            output_dir=params.output_dir,
            dataset_name=params.name,
            aug_per_image=params.aug_per_image,
            rotation=params.rotation,
            translation=params.translation,
            scale=params.scale,
            noise=params.noise,
            brightness=params.brightness,
            contrast=params.contrast,
            flip_h=params.flip_h,
            flip_v=params.flip_v,
            on_error=self.augment_error.emit,
            on_done=self.augment_done.emit,
            on_progress=self.augment_progress.emit
        )
        self.augment_service = service
        self.augment_worker = Worker.start_task(task=service.augment_dataset, error_cb=self.augment_error.emit)
        # self.worker.start()

    @qtc.Slot(object)
    def _on_augment_done(self, results: AugmentorResults):
        msg = (
        f"\n"
        f"Bilder:      {results.total_imgs}\n"
        f"Augmentiert: {results.success}/{results.total_aug_imgs}\n"
        f"Fehler:      {results.error}"
    )
        self.view.show_augment_progress(msg)
        self.view.update_augment_button(False)

    @qtc.Slot(int, int)
    def _on_augment_progress(self, count:int, total_count:int):
        progress = (count/total_count) * 100
        self.view.show_augment_progress_bar(progress)

    @qtc.Slot(str)
    def _on_augment_progress_error(self, msg:str):
        self.view.show_augment_progress(msg)

    @qtc.Slot(str)
    def _on_augment_error(self, msg:str):
        self.view.show_warning_message(f"Fehler beim Augmentieren!\n\n{msg}")
        self.view.update_augment_button(False)



    @qtc.Slot()
    def _on_select_dataset_augment_path(self):
        folder_path =  qtw.QFileDialog.getExistingDirectory(self.view, "Speicherort auswählen")
        if not folder_path:
            return
        self.view.set_dataset_path_augment(folder_path) 


    #----- create
    @qtc.Slot()
    def _on_create_dataset(self):
        if self.create_worker and self.create_worker.isRunning():
            logger.debug("Datensatzerstellung läuft → Abbruch wird angefordert")
            self.create_service.cancel()
            # self.view.show_warning_message("\nDatensatzerstellung abgebrochen!")
            self.view.show_creation_progress_bar(0)
            self.view.update_create_button(False)
            return
        if not self.app_state_ui.dataset_path:
            self.view.show_warning_message("Kein Datensatz ausgewählt!")
            return
        params = self.view.get_dataset_creation_parameters()
        if not params.class_names:
            self.view.show_warning_message("Bitte mindestens einen Klassennamen angeben!")
            return
        logging.debug("Starte Datensatzerstellung")
        self.view.update_create_button(True)
        kwargs = {
            "source_path":self.app_state_ui.dataset_path,
            "target_path":params.target_path,
            "dataset_name":params.name,
            "class_names":params.class_names,
            "imgsz":params.img_size,
            "train_size":params.train_split/100.0,
            "val_size":params.val_split/100.0,
            "test_size":params.test_split/100.0,
            "progress_callback": self.creation_progress.emit 
        }
        self.create_service = DatasetCreationService()

        self.create_worker = Worker.start_task(task=self.create_service.generate_dataset,finished_cb=self.creation_done.emit, error_cb=self.creation_error.emit, **kwargs )

    @qtc.Slot()
    def _on_select_dataset_creation_path(self):
        folder_path =  qtw.QFileDialog.getExistingDirectory(self.view, "Speicherort auswählen")
        if not folder_path:
            return
        self.view.set_dataset_path_create(folder_path) 

    @qtc.Slot()
    def _on_creation_done(self, path:Path):
        if path:
            self.view.show_info_message(f"Datensatz erstellt:\n{path}")
        self.view.update_create_button(False)

    @qtc.Slot(str)
    def _on_creation_error(self, msg:str):
        if msg == "Cancel":
            self.view.show_warning_message("Datensatzerstellung abgebrochen!")
        else:
            self.view.show_warning_message(f"Fehler beim Erstellen!\n\n{msg}")
        self.view.update_create_button(False)

    @qtc.Slot(int, int)
    def _on_creation_progress(self, count:int, total_count:int):
        progress = (count/total_count) * 100
        self.view.show_creation_progress_bar(progress)

    # #---- scale
    # @qtc.Slot()
    # def _on_scale_dataset(self):
    #     logging.debug("Starte Datensatzskalierung")
    #     if not self.app_state_ui.dataset_path:
    #         self.view.show_warning_message("Kein Datensatz ausgewählt!")
    #         return
    #     params = self.view.get_dataset_scaling_parameters()
    #     service = ScalingService(dataset_path=self.app_state_ui.dataset_path, method=params.method)
    #     self.worker = Worker(task=service.normalize)
    #     self.worker.start()