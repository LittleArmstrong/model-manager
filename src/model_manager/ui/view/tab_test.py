
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from dataclasses import dataclass

from model_manager.ui.designer.tab_test_ui import Ui_TestTab


@dataclass
class TestingParametersUI:
    model_name: str
    model_size: str
    use_last_model: bool
    batch_size: int
    min_score: float
    min_nms_iou: float


class TestTab(qtw.QWidget, Ui_TestTab):
    import_weights_pushed = qtc.Signal()
    testing_started = qtc.Signal()
    next_image = qtc.Signal()
    previous_image = qtc.Signal()
    img_order_changed = qtc.Signal(str)
    use_last_model_toggled = qtc.Signal(bool)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self._setup_table()

        self.btn_import_weights.clicked.connect(self.import_weights_pushed)
        self.btn_start_testing.clicked.connect(self.testing_started)
        self.btn_next_img.clicked.connect(self.next_image)
        self.btn_prev_img.clicked.connect(self.previous_image)
        self.cmb_sort_order.currentTextChanged.connect(self.img_order_changed)
        self.chb_last_model.toggled.connect(self.use_last_model_toggled)


    def set_model_weights_file_name(self, file_name:str):
        self.lbl_model_weights.setText(file_name)

    def get_test_parameters(self) -> TestingParametersUI:
        return TestingParametersUI(
            model_name=self.cmb_selected_model.currentText(),
            model_size=self.cmb_selected_size.currentText(),
            use_last_model=self.chb_last_model.isChecked(),
            batch_size = self.spin_batch_size.value(),
            min_score=self.dspin_min_score.value(),
            min_nms_iou=self.dspin_min_nms_iou.value()
        )
    
    # def get_min_confidence_score(self) -> float:
    #     return self.dspin_min_confidence.value()

    def set_models(self, models: tuple, model_sizes: tuple):
        self.cmb_selected_model.clear()
        self.cmb_selected_model.addItems(models)
        if models:
            self.cmb_selected_model.setCurrentIndex(0)
        self.cmb_selected_size.clear()
        self.cmb_selected_size.addItems(model_sizes)
        if model_sizes:
            self.cmb_selected_model.setCurrentIndex(0)

    def set_table_results_model(self, model:qtc.QAbstractTableModel):
        self.table_results_view.setModel(model)
        self._style_table()

    def show_image(self, img:bytearray):
        pixmap = qtg.QPixmap()
        pixmap.loadFromData(img)
        self.img_preview.setPixmap(pixmap)

    def clear_image(self):
        self.img_preview.clear()

    def set_progress_bar(self, value:int):
        self.pb_progress_bar.setValue(value)

    def clear_output(self):
        self.set_progress_bar(0)
        self.clear_image()

    def set_import_weigths_state(self, disable=True):
        self.btn_import_weights.setDisabled(disable)
        self.lbl_model_weights.setDisabled(disable)

    def set_model_state(self, disable=True):
        self.cmb_selected_model.setDisabled(disable)
        self.cmb_selected_size.setDisabled(disable)


    def show_warning_message(self, msg, title = "Warnung"):
        qtw.QMessageBox.warning(self, title, msg)

    def show_error_message(self, msg, title = "Fehler"):
        qtw.QMessageBox.critical(self, title, msg)


    def update_test_button(self, running: bool):
        self.btn_start_testing.setText("Abbrechen" if running else "Starte Test")
        self.btn_start_testing.setToolTip(
            "Bricht das Testen beim nächsten Batchstart ab."
            if running
            else "Testet die Modellleistung am ausgewählten Datensatz."
        )

    def set_model(self, name, size):
        # Modell auswählen
        idx_model = self.cmb_selected_model.findText(name, qtc.Qt.MatchFlag.MatchFixedString)
        if idx_model >= 0:
            self.cmb_selected_model.setCurrentIndex(idx_model)

        # Größe auswählen
        idx_size = self.cmb_selected_size.findText(size, qtc.Qt.MatchFlag.MatchFixedString)
        if idx_size >= 0:
            self.cmb_selected_size.setCurrentIndex(idx_size)



# ---------------------------------------------


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