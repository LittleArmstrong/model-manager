import os
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
import logging

from model_manager.ui.view.tab_training import TrainingTab
from model_manager.application.service.training_service import YoloTrainingService, TrainingResults, TrainingProgress
from model_manager.controller.app_state import AppStateUI
from model_manager.controller.worker import Worker
from pathlib import Path
from ultralytics.models.yolo.detect import DetectionTrainer
from model_manager.controller.models import MetricsTableModel
from model_manager.application.service.info_service import InfoService
import torch

logger = logging.getLogger(__name__)

class TrainingController(qtc.QObject):
    training_start = qtc.Signal(object)
    batch_end = qtc.Signal(object, object) 
    # epoch_start = qtc.Signal(object)
    epoch_end = qtc.Signal(object)
    training_end = qtc.Signal(object)
    training_error = qtc.Signal(str)

    def __init__(self, view:TrainingTab, app_state_ui:AppStateUI):
        super().__init__()
        self.app_state_ui = app_state_ui
        self.view = view

        self.worker = None
        self.training_service = None
        self.model_weights_path = None
        self.plot_curves = {}
        self.plot_data = {"epoch": []}
        self.train_results = None

        self.results_model = MetricsTableModel()
        self.view.set_table_results_model(self.results_model)

        self.view.set_optimizers(InfoService.YOLO_OPTIMIZERS)
        self.view.set_learning_rate_state(disable=True)

        self.view.set_models(InfoService.YOLO_MODELS)
        self.view.set_model_types(InfoService.YOLO_MODEL_SIZES)
        model_info = InfoService.get_model_info(InfoService.YOLO_MODELS[0])
        self.view.set_model_info(model_info.backbone_stages, model_info.head_stages, model_info.max_freeze)
        self.view.set_freeze_layers_state(disable=True)

        self.training_start.connect(self._on_training_start)
        # self.epoch_start.connect(self._on_epoch_start)
        self.epoch_end.connect(self._on_epoch_end)
        self.batch_end.connect(self._on_batch_end)
        self.training_end.connect(self._on_training_end)
        self.training_error.connect(self._on_training_error)

        self.view.btn_start_training.clicked.connect(self._start_training)
        self.view.optimizer_changed.connect(self._on_optimizer_changed)
        self.view.transfer_learning_changed.connect(self._on_transfer_lerning_changed)
        self.view.btn_import_weights.clicked.connect(self._on_import_weights)
        self.view.use_pretrained_model_changed.connect(self._on_pretrained_model_changed)
        self.view.model_choice_changed.connect(self._on_model_choice_changed)

        self.view.resume_training_changed.connect(self._on_resume_training_changed)
        

        
    def _start_training(self):
        if self.worker and self.worker.isRunning():
            logger.debug("Training läuft → Abbruch wird angefordert")
            self.training_service.cancel()
            self.view.append_progress("\nAbbruch angefordert! Training wird beim nächsten Batch-Start abgebrochen ...")
            self.view.append_progress("")
            return
        logging.info("Training gestartet.")

        if not self.app_state_ui.dataset_path:
            logging.info("Training gestartet, aber kein Datensatz ausgewählt.")
            self.view.show_warning_message("Kein Datensatz ausgewählt!")
            self._on_training_finished()
            return
        
        self.view.update_training_button(running=True)
        self.view.clear_output()
        self.results_model.clear()
        
        # get ui values
        parameters = self.view.get_parameters()

  
        self.training_service = YoloTrainingService(
            dataset_path=self.app_state_ui.dataset_path,
            model_name=parameters.model_name,
            model_size=parameters.model_type,
            pretrained=parameters.use_pretrained_model,
            apply_transfer_learning=parameters.apply_transfer_learning,
            freeze=parameters.freeze_layers,
            imgsz=parameters.input_size,
            batch=parameters.batch_size,
            epochs=parameters.epochs,
            optimizer=parameters.optimizer,
            lr0=parameters.initial_learning_rate,
            weight_decay=parameters.weight_decay,
            weights_path=self.model_weights_path,
            resume_training=parameters.resume_training,
            on_train_start=[self.training_start.emit],
            on_train_batch_end=[self.batch_end.emit],
            # on_train_epoch_start=[self.epoch_start.emit],
            on_train_epoch_end=[self.epoch_end.emit],
            on_train_end=[self.training_end.emit],
            on_error=[self.training_error.emit]
        )

        self.worker = Worker(task=self.training_service.start_training)
        self.worker.finished.connect(self._on_training_finished)
        self.worker.error.connect(self._on_training_error)
        self.worker.start()


    @qtc.Slot()
    def _select_model_path(self):
        folder_path = qtw.QFileDialog.getExistingDirectory(self.view, "Gewichte auswählen", "PyTorch-YOLO-Modell (*.pt)")
        if not folder_path:
            return
        logger.info("Gewichte ausgewählt")
        self.model_weights_path = folder_path
        model_weights_name = os.path.basename(folder_path)
        self.view.set_model_weights(model_weights_name) 



    @qtc.Slot(object)
    def _on_training_start(self, trainer: DetectionTrainer):
        if self.training_service.resume:
            self.view.append_progress("Training wird weitergeführt ...")
        else:
            self.view.append_progress("Training wird gestartet ...")
            
        self.view.append_progress("\n")



    @qtc.Slot(object, object)
    def _on_batch_end(self, trainer: DetectionTrainer, progress:TrainingProgress):
        epoch_batch = progress.batch_count
        self.view.update_last_progress(f"Batch {epoch_batch} / {progress.batches_per_epoch}")
        try:
            progress = int(((progress.epoch * progress.batches_per_epoch + progress.batch_count) / (progress.epochs * progress.batches_per_epoch)) * 100)
        except Exception as e:
            progress = 0
            logger.exception(e)
        self.view.set_progress_bar(progress)



    # @qtc.Slot(object)
    # def _on_epoch_start(self, trainer: DetectionTrainer):
    #     pass


    
    def _remap_results(self, results):
        mapping = {
            "train/box_loss": "box_loss",
            "train/cls_loss": "class_loss",
            "train/dfl_loss": "dfl_loss",
            "metrics/precision(B)": "precision",
            "metrics/recall(B)": "recall",
            "metrics/mAP50(B)": "mAP@50",
            "metrics/mAP50-95(B)": "mAP@50-95",
            'val/box_loss': "val_box_loss", 
            'val/cls_loss': "val_cls_loss",
            'val/dfl_loss': "val_dfl_loss"
        }
        return { mapping.get(k, k): v for k, v in results.items() }


    @qtc.Slot(object)
    def _on_epoch_end(self, trainer: DetectionTrainer):
        self.view.update_last_progress("")
        # TODO untige Berechnung soll nicht im Controller gemacht werden sondern im service
        self.view.append_progress(trainer.progress_string())
        loss_length = trainer.tloss.shape[0] if len(trainer.tloss.shape) else 1
        data = (
            ("%11s" * 2 + "%11.4g" * (2 + loss_length))
            % (
                f"{trainer.epoch + 1}/{trainer.epochs}",
                f"{trainer._get_memory():.3g}G",
                *(trainer.tloss if loss_length > 1 else torch.unsqueeze(self.tloss, 0)),
                self.training_service.batch,
                self.training_service.imgsz,
            )
        )
        self.view.append_progress(data)
        self.view.append_progress("")
        self.view.append_progress("")

        # # plot
        # remapped_results = self._remap_results(results)
        # self.view.set_graph_data(x=results["epoch"],y=remapped_results)
        # metrics = trainer.metrics
        metrics={**trainer.label_loss_items(trainer.tloss), **trainer.metrics}
        remapped = self._remap_results(metrics)
        self.view.append_graph_metrics(trainer.epoch + 1, remapped)




    @qtc.Slot(object)
    def _on_training_end(self, results: TrainingResults):
        # self._on_epoch_start(results.trainer)
        # table_data = self._build_table_data(summary)
        # self.view.set_table_data(table_data)
        self.view.append_progress("\nTraining beendet!")
        self.train_results = results
        self.results_model.setRows(results.metrics)        


    def _build_table_data(self, summary):
        classes = summary.get("classes", {})
        class_results = summary.get("class_results", [])
        overall = summary.get("results", {})

        table_data = []

        overall_row = [
            "Gesamt",
            str(overall.get("images", 0)),
            str(overall.get("instances", 0)),
            f"{overall.get('metrics/precision(B)', 0):.3f}",
            f"{overall.get('metrics/recall(B)', 0):.3f}",
            f"{overall.get('metrics/f1-score(B)', 0):.3f}",
            f"{overall.get('metrics/mAP50(B)', 0):.3f}",
            f"{overall.get('metrics/mAP50-95(B)', 0):.3f}",
        ]
        table_data.append(overall_row)

        for _, cls_name in classes.items():
            # passender Eintrag in class_results finden
            res = next((r for r in class_results if r.get("Class") == cls_name), None)

            if res:
                row = [
                    cls_name,
                    str(res.get("Images", 0)),
                    str(res.get("Instances", 0)),
                    f"{res.get('Box-P', 0):.3f}",
                    f"{res.get('Box-R', 0):.3f}",
                    f"{res.get('Box-F1', 0):.3f}",
                    f"{res.get('mAP50', 0):.3f}",
                    f"{res.get('mAP50-95', 0):.3f}",
                ]
            else:
                # Wenn keine Ergebnisse existieren → alles 0
                row = [
                    cls_name,
                    "0",
                    "0",
                    "0.000",
                    "0.000",
                    "0.000",
                    "0.000",
                    "0.000",
                ]

            table_data.append(row)

        return table_data


    qtc.Slot(str)
    def _on_optimizer_changed(self, optimizer:str):
        self.view.set_learning_rate_state(disable = (optimizer == 'auto'))

    qtc.Slot(bool)
    def _on_transfer_lerning_changed(self, checked: bool):
        self.view.set_freeze_layers_state(disable = not checked)    

    qtc.Slot(bool)
    def _on_pretrained_model_changed(self, checked: bool):
        self.view.set_import_weights_state(disable = checked)    
        self.view.set_resume_training_state(disable = checked)    
        self.view.set_resume_training_value(False)    

    qtc.Slot(bool)
    def _on_model_choice_changed(self, model: str):
        model_info = InfoService.get_model_info(model)
        if not model_info:
            return
        self.view.set_model_info(model_info.backbone_stages, model_info.head_stages, model_info.max_freeze)

    qtc.Slot(bool)
    def _on_resume_training_changed(self, checked: bool):
        imported = bool(self.model_weights_path) 
        self.view.update_resume_training_text(checked, imported)



    @qtc.Slot(str)
    def _on_training_error(self, msg:str):
        if 'Resume checkpoint not found' in msg:
            self.view.show_error_message("Modell hat kein Checkpoint! Training kann nicht fortgeführt werden.\nBitte trainiere normal weiter oder wähle ein anderes Modell aus.")
        elif "nothing to resume" in msg:
            self.view.show_error_message("Modell wurde schon zu Ende trainiert!\nBitte trainiere normal weiter.")
        elif "Training wurde abgebrochen" in msg:
            self.view.show_error_message(msg)
            self.view.append_progress(msg)
        else:
            self.view.show_error_message(msg)

    @qtc.Slot(str)
    def _on_training_finished(self, results:dict|None=None):
        self.view.update_training_button(running=False)

    @qtc.Slot(str)
    def on_training_canceled(self, msg:str):
        self.view.append_progress("")
        self.view.append_progress("\nTraining abgebrochen!")

    @qtc.Slot()
    def _on_import_weights(self):
        if self.model_weights_path:
            self.model_weights_path = ""
            self.view.set_model_weights_file_name("keine Gewichte importiert")
            self.view.update_weights_button(imported=False)
            return
        file_path = qtw.QFileDialog.getOpenFileName(self.view, caption="Gewichte auswählen", filter="PyTorch-YOLO-Modell (*.pt)")[0]
        if not file_path:
            return
        self.model_weights_path = Path(file_path)
        self.view.set_model_weights_file_name(self.model_weights_path.name) 
        self.view.update_weights_button(imported=True)


    