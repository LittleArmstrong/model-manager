import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from model_manager.ui.designer.tab_training_ui import Ui_TrainingTab
import pyqtgraph as pg
from dataclasses import dataclass

@dataclass
class TrainingParametersUI:
    model_name: str
    model_type: str
    use_pretrained_model: bool 
    apply_transfer_learning: bool
    freeze_layers: int 
    input_size: int
    batch_size: int
    epochs: int
    optimizer: str
    initial_learning_rate: float
    weight_decay: float
    model_weights_path: str | None = None 
    resume_training:bool = False



class TrainingTab(qtw.QWidget, Ui_TrainingTab):
    optimizer_changed = qtc.Signal(str)
    transfer_learning_changed = qtc.Signal(bool)
    use_pretrained_model_changed = qtc.Signal(bool)
    model_choice_changed = qtc.Signal(str)
    resume_training_changed = qtc.Signal(bool)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.chb_resume_training.setVisible(False)
        self._epochs = []
        self._plot_curves = {}
        self._setup_graph()
        self._setup_metrics_graph()
        # self._setup_table()
        self._graph_data = {key: [] for key in self._plot_curves.keys()}

        self.cmb_optimizer.currentTextChanged.connect(self.optimizer_changed)
        self.chb_transfer_learning.toggled.connect(self.transfer_learning_changed)
        self.chb_pretrained.toggled.connect(self.use_pretrained_model_changed)
        self.cmb_selected_model.currentTextChanged.connect(self.model_choice_changed)
        self.chb_resume_training.toggled.connect(self.resume_training_changed)

    def set_model_weights(self, name:str):
        self.lbl_model_weights.setText(name)

    
    def get_parameters(self) -> TrainingParametersUI:
        return TrainingParametersUI(
            model_name=self.cmb_selected_model.currentText(),
            model_type=self.cmb_selected_model_type.currentText(),
            use_pretrained_model=self.chb_pretrained.isChecked(),
            apply_transfer_learning=self.chb_transfer_learning.isChecked(),
            freeze_layers=self.spin_freeze_layers.value(),
            input_size=self.spin_image_size.value(),
            batch_size=self.spin_batch_size.value(),
            epochs=self.spin_epochs.value(),
            optimizer=self.cmb_optimizer.currentText(),
            initial_learning_rate=self.dspin_initial_lr.value(),
            weight_decay=self.dspin_weight_decay.value(),
            resume_training=self.chb_resume_training.isChecked()
            # resume_training=False
        )
    

    def show_error_message(self, message:str):
        self.lbl_status_message.setText(message)

    def set_progress_bar(self, value:int):
        self.pb_progress_bar.setValue(value)

    def append_progress(self, message:str):
        self.ptxt_process_output.appendPlainText(message)

    def update_last_progress(self, message: str):
        """
        Ersetzt den Inhalt der letzten Zeile im QPlainTextEdit mit der neuen Nachricht.
        """
        text_edit = self.ptxt_process_output
        cursor = text_edit.textCursor()

        # 1. Cursor ans Ende bewegen, um sicherzustellen, dass wir in der letzten Zeile sind.
        cursor.movePosition(qtg.QTextCursor.End)
        
        # 2. Zum Anfang der aktuellen Zeile springen (StartOfLine).
        cursor.movePosition(qtg.QTextCursor.StartOfLine) 
        
        # 3. Den gesamten Inhalt von dieser Position bis zum Ende der Zeile auswählen (EndOfLine).
        # Der Zeilenumbruch (falls vorhanden) wird ebenfalls markiert.
        cursor.movePosition(qtg.QTextCursor.EndOfLine, qtg.QTextCursor.KeepAnchor)
        
        # 4. Ausgewählten Text entfernen (Die Zeile wird gelöscht).
        cursor.removeSelectedText()
        
        # 5. Neuen Text einfügen.
        cursor.insertText(message)
        
        # Sicherstellen, dass die letzte Zeile sichtbar ist (optional, aber nützlich).
        text_edit.setTextCursor(cursor)


    def set_table_data(self, data: list[list[str]]):
        table = self.table_results
        table.setRowCount(len(data))
        for i, row in enumerate(data):
            for j, val in enumerate(row):
                table.setItem(i, j, qtw.QTableWidgetItem(val))

    def set_graph_data(self, x, y):
        for key, curve in self._plot_curves.items():
            curve.setData(x, y[key])
    
    def append_graph_metrics(self, epoch: int, metrics: dict):
        self._epochs.append(epoch)

        for key, curve in self._plot_curves.items():
            if key in metrics:
                self._graph_data[key].append(metrics[key])
                curve.setData(self._epochs, self._graph_data[key])

    def clear_graph(self):
        self._epochs = []
        for curve in self._plot_curves.values():
            curve.setData([], [])
        self._graph_data = {key: [] for key in self._plot_curves.keys()}
    
    def clear_output(self):
        self.clear_graph()
        self.set_progress_bar(0)
        self.ptxt_process_output.clear()


    def set_optimizers(self, optimizers: tuple):
        self.cmb_optimizer.clear()
        self.cmb_optimizer.addItems(optimizers)
        if optimizers:
            self.cmb_optimizer.setCurrentIndex(0) 


    def set_learning_rate_state(self, disable=False):
        self.dspin_initial_lr.setDisabled(disable)

    def set_models(self, models: tuple):
        self.cmb_selected_model.clear()
        self.cmb_selected_model.addItems(models)
        if models:
            self.cmb_selected_model.setCurrentIndex(0)

    def set_model_types(self, model_types: tuple):
        self.cmb_selected_model_type.clear()
        self.cmb_selected_model_type.addItems(model_types)
        if model_types:
            self.cmb_selected_model_type.setCurrentIndex(0)

    def set_freeze_layers_state(self, disable=False):
        self.spin_freeze_layers.setDisabled(disable)

    def set_import_weights_state(self, disable=False):
        self.btn_import_weights.setDisabled(disable)

    def set_resume_training_state(self,disable=False):
        self.chb_resume_training.setDisabled(disable)

    def set_resume_training_value(self, checked):
        self.chb_resume_training.setChecked(checked)

    def show_warning_message(self, msg, title = "Warnung"):
        qtw.QMessageBox.warning(self, title, msg)

    def show_error_message(self, msg, title = "Fehler"):
        qtw.QMessageBox.critical(self, title, msg)

    def update_training_button(self, running: bool):
        self.btn_start_training.setText("Abbrechen" if running else "Starte Training")
        self.btn_start_training.setToolTip(
            "Bricht das Training beim nächsten Batchstart ab."
            if running
            else "Trainiert ein Modell mit allen gegebenen Parameter am ausgewählten Datensatz."
        )

    def update_weights_button(self, imported: bool):
        text = "Gewichte entfernen" if imported else "Gewichte importieren"
        if self.chb_resume_training.isChecked():
            text = "Modell entfernen" if imported else "Modell importieren"
            
        self.btn_import_weights.setText(text)
        self.btn_import_weights.setToolTip(
            "Gewichte/Modell entfernen."
            if imported
            else "Auswahl der Gewichte bzw. des Modells zum importieren."
        )

    def set_model_weights_file_name(self, file_name:str):
        self.lbl_model_weights.setText(file_name)

    def set_table_results_model(self, model:qtc.QAbstractTableModel):
        self.table_results_view.setModel(model)
        self._style_table()

    def set_model_info(self, backbone_layer:int, head_layer:int, max_freeze:int):
        self.lbl_backbone_layer.setText(str(backbone_layer))
        self.lbl_head_layer.setText(str(head_layer))
        self.lbl_max_freeze.setText(str(max_freeze))

    def update_resume_training_text(self, checked:bool, imported:bool):
        lbl_text = "keine Gewichte importiert"
        btn_text = "Gewichte entfernen" if imported else "Gewichte importieren"
        # btn_text = "Gewichte importieren"
        if checked:
            lbl_text = "kein Modell importiert"
            btn_text = "Modell entfernen" if imported else "Modell importieren"
        if not imported:
            self.lbl_model_weights.setText(lbl_text)
        self.btn_import_weights.setText(btn_text)



    
        

# -----------------------------------



    def _setup_graph(self):
        pg.setConfigOption('background', 'w')  # weißer Hintergrund
        pg.setConfigOption('foreground', 'k')  # schwarze Achsen & Texte
        self.graph_results = pg.PlotWidget()
        self.graph_results.getAxis('bottom').setTickSpacing(1, 1)  # Nur ganze Zahlen (Epochs)
        self.graph_results.getAxis('bottom').setStyle(tickTextOffset=10)
        self.graph_results.getAxis('bottom').setTickFont(pg.QtGui.QFont("Arial", 9))
        self.graph_results.getAxis('left').setTickFont(pg.QtGui.QFont("Arial", 9))
        legend = self.graph_results.addLegend()
        legend.setBrush(pg.mkBrush(255, 255, 255, 255))       # Hintergrund (RGBA)
        legend.setPen(pg.mkPen(color=(0, 0, 0), width=1))     # Rahmen
        self.graph_results.setLabel("bottom", "Epoche")
        self.graph_results.setLabel("left", "Wert")
        self.graph_results.setXRange(1, 10, padding=0)


        # Ersetze QGraphicsView mit echtem Plot
        layout = self.graph_results_placeholder.parent().layout()
        layout.replaceWidget(self.graph_results_placeholder, self.graph_results)
        self.graph_results_placeholder.deleteLater()  # Platzhalter löschen


        metric_colors = {
            "box_loss": "r",
            "class_loss": "g",
            "dfl_loss": "b",
            "val_box_loss": "orange",
            "val_class_loss": "m",
            "val_dfl_loss": "c"
        }

        graph = self.graph_results
        for metric, color in metric_colors.items():
            pen = pg.mkPen(color=color, width=2)
            self._plot_curves[metric] = graph.plot(name=metric, pen=pen)

    def _setup_metrics_graph(self):
        pg.setConfigOption('background', 'w')  # weißer Hintergrund
        pg.setConfigOption('foreground', 'k')  # schwarze Achsen & Texte
        self.graph_metrics = pg.PlotWidget()
        self.graph_metrics.getAxis('bottom').setTickSpacing(1, 1)  # Nur ganze Zahlen (Epochs)
        self.graph_metrics.getAxis('bottom').setStyle(tickTextOffset=10)
        self.graph_metrics.getAxis('bottom').setTickFont(pg.QtGui.QFont("Arial", 9))
        self.graph_metrics.getAxis('left').setTickFont(pg.QtGui.QFont("Arial", 9))
        legend = self.graph_metrics.addLegend()
        legend.setBrush(pg.mkBrush(255, 255, 255, 255))       # Hintergrund (RGBA)
        legend.setPen(pg.mkPen(color=(0, 0, 0), width=1))     # Rahmen
        self.graph_metrics.setLabel("bottom", "Epoche")
        self.graph_metrics.setLabel("left", "Wert")
        self.graph_metrics.setXRange(1, 10, padding=0)


        # Ersetze QGraphicsView mit echtem Plot
        layout = self.graph_metrics_placeholder.parent().layout()
        layout.replaceWidget(self.graph_metrics_placeholder, self.graph_metrics)
        self.graph_metrics_placeholder.deleteLater()  # Platzhalter löschen


        metric_colors = {
            "precision": "orange",
            "recall": "m",
            "mAP@50": "c",
            "mAP@50-95": "k"
        }

        graph = self.graph_metrics
        for metric, color in metric_colors.items():
            pen = pg.mkPen(color=color, width=2)
            self._plot_curves[metric] = graph.plot(name=metric, pen=pen)

    
    def _style_table(self):
        table = self.table_results_view
        table.resizeColumnsToContents()
        table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        table.horizontalHeader().setDefaultAlignment(
            qtc.Qt.AlignLeft | qtc.Qt.AlignVCenter
        )
        table.verticalHeader().setVisible(False)
        table.setAlternatingRowColors(True)

    # def _setup_table(self):
    #     table = self.table_results
    #     headers = [
    #         "Klasse",
    #         "Bilder",
    #         "Instanzen",
    #         "Präzision",
    #         "Recall",
    #         "F1",
    #         "mAP@50",
    #         "mAP@50-95"
    #     ]
    #     table.reset()
    #     table.setColumnCount(len(headers))
    #     table.setHorizontalHeaderLabels(headers)
    #     table.resizeColumnsToContents()
    #     table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
    #     table.verticalHeader().setVisible(False)
    #     table.setAlternatingRowColors(True)
    #     table.setEditTriggers(qtw.QTableWidget.NoEditTriggers)


    
    
    # def create_curve(self):
    #     for key, curve in self.plot_curves.items():
    #         curve.setData(self.plot_data["epoch"], self.plot_data[key])

       


    # def _populate_models(self):
    #     """Befüllt die Modell-Combobox mit den verfügbaren YOLO-Versionen."""
    #     self.selected_model.clear()
    #     self.selected_model.addItems(MODELS.keys())
    #     self.selected_model.setCurrentIndex(0)
    #     self._populate_types(list(MODELS.keys())[0])

    # def _populate_types(self, model_name: str):
    #     """Aktualisiert die Typen-Combobox je nach Modell."""
    #     self.selected_model_type.clear()
    #     model_info = MODELS.get(model_name, {})
    #     types = model_info.get("types", [])
    #     self.selected_model_type.addItems(types)

    # def _populate_optimizers(self):
    #     """Befüllt die Optimizer-Combobox (aktuell nur YOLO)."""
    #     self.optimizer.addItems(OPTIMIZERS["yolo"])