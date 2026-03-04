# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_training.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGraphicsView, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QPlainTextEdit,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_TrainingTab(object):
    def setupUi(self, TrainingTab):
        if not TrainingTab.objectName():
            TrainingTab.setObjectName(u"TrainingTab")
        TrainingTab.resize(913, 847)
        self.gridLayout = QGridLayout(TrainingTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(TrainingTab)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.chb_pretrained = QCheckBox(self.groupBox_3)
        self.chb_pretrained.setObjectName(u"chb_pretrained")

        self.gridLayout_3.addWidget(self.chb_pretrained, 0, 2, 1, 1)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(96, 0))

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.lbl_model_weights = QLabel(self.groupBox_3)
        self.lbl_model_weights.setObjectName(u"lbl_model_weights")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_model_weights.sizePolicy().hasHeightForWidth())
        self.lbl_model_weights.setSizePolicy(sizePolicy)
        self.lbl_model_weights.setMinimumSize(QSize(134, 0))
        font = QFont()
        font.setItalic(True)
        self.lbl_model_weights.setFont(font)
        self.lbl_model_weights.setTextFormat(Qt.TextFormat.PlainText)

        self.gridLayout_3.addWidget(self.lbl_model_weights, 2, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(96, 0))

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(96, 0))

        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)

        self.btn_import_weights = QPushButton(self.groupBox_3)
        self.btn_import_weights.setObjectName(u"btn_import_weights")

        self.gridLayout_3.addWidget(self.btn_import_weights, 2, 2, 1, 1)

        self.cmb_selected_model_type = QComboBox(self.groupBox_3)
        self.cmb_selected_model_type.addItem("")
        self.cmb_selected_model_type.addItem("")
        self.cmb_selected_model_type.addItem("")
        self.cmb_selected_model_type.addItem("")
        self.cmb_selected_model_type.addItem("")
        self.cmb_selected_model_type.setObjectName(u"cmb_selected_model_type")
        self.cmb_selected_model_type.setMinimumSize(QSize(115, 0))

        self.gridLayout_3.addWidget(self.cmb_selected_model_type, 1, 1, 1, 1)

        self.cmb_selected_model = QComboBox(self.groupBox_3)
        self.cmb_selected_model.addItem("")
        self.cmb_selected_model.setObjectName(u"cmb_selected_model")
        self.cmb_selected_model.setMinimumSize(QSize(115, 0))

        self.gridLayout_3.addWidget(self.cmb_selected_model, 0, 1, 1, 1)

        self.chb_resume_training = QCheckBox(self.groupBox_3)
        self.chb_resume_training.setObjectName(u"chb_resume_training")
        self.chb_resume_training.setEnabled(True)

        self.gridLayout_3.addWidget(self.chb_resume_training, 2, 3, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.groupBox_6 = QGroupBox(self.widget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(256, 0))
        self.gridLayout_6 = QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_12 = QLabel(self.groupBox_6)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 0, 0, 1, 1)

        self.lbl_head_layer = QLabel(self.groupBox_6)
        self.lbl_head_layer.setObjectName(u"lbl_head_layer")

        self.gridLayout_6.addWidget(self.lbl_head_layer, 1, 1, 1, 1)

        self.lbl_backbone_layer = QLabel(self.groupBox_6)
        self.lbl_backbone_layer.setObjectName(u"lbl_backbone_layer")

        self.gridLayout_6.addWidget(self.lbl_backbone_layer, 0, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_6)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_16 = QLabel(self.groupBox_6)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_6.addWidget(self.label_16, 2, 0, 1, 1)

        self.lbl_max_freeze = QLabel(self.groupBox_6)
        self.lbl_max_freeze.setObjectName(u"lbl_max_freeze")

        self.gridLayout_6.addWidget(self.lbl_max_freeze, 2, 1, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_6)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.btn_start_training = QPushButton(TrainingTab)
        self.btn_start_training.setObjectName(u"btn_start_training")

        self.gridLayout.addWidget(self.btn_start_training, 7, 0, 1, 1)

        self.pb_progress_bar = QProgressBar(TrainingTab)
        self.pb_progress_bar.setObjectName(u"pb_progress_bar")
        self.pb_progress_bar.setValue(0)

        self.gridLayout.addWidget(self.pb_progress_bar, 6, 0, 1, 1)

        self.groupBox_2 = QGroupBox(TrainingTab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.groupBox_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.output = QWidget()
        self.output.setObjectName(u"output")
        self.verticalLayout_2 = QVBoxLayout(self.output)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ptxt_process_output = QPlainTextEdit(self.output)
        self.ptxt_process_output.setObjectName(u"ptxt_process_output")
        self.ptxt_process_output.setMinimumSize(QSize(115, 0))
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(10)
        self.ptxt_process_output.setFont(font1)
        self.ptxt_process_output.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.ptxt_process_output)

        self.tabWidget.addTab(self.output, "")
        self.graphs = QWidget()
        self.graphs.setObjectName(u"graphs")
        self.verticalLayout_3 = QVBoxLayout(self.graphs)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget_2 = QTabWidget(self.graphs)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.loss = QWidget()
        self.loss.setObjectName(u"loss")
        self.verticalLayout_5 = QVBoxLayout(self.loss)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.graph_results_placeholder = QGraphicsView(self.loss)
        self.graph_results_placeholder.setObjectName(u"graph_results_placeholder")

        self.verticalLayout_5.addWidget(self.graph_results_placeholder)

        self.tabWidget_2.addTab(self.loss, "")
        self.metric = QWidget()
        self.metric.setObjectName(u"metric")
        self.verticalLayout_6 = QVBoxLayout(self.metric)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.graph_metrics_placeholder = QGraphicsView(self.metric)
        self.graph_metrics_placeholder.setObjectName(u"graph_metrics_placeholder")

        self.verticalLayout_6.addWidget(self.graph_metrics_placeholder)

        self.tabWidget_2.addTab(self.metric, "")

        self.verticalLayout_3.addWidget(self.tabWidget_2)

        self.tabWidget.addTab(self.graphs, "")
        self.results = QWidget()
        self.results.setObjectName(u"results")
        self.verticalLayout_4 = QVBoxLayout(self.results)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.table_results_view = QTableView(self.results)
        self.table_results_view.setObjectName(u"table_results_view")

        self.verticalLayout_4.addWidget(self.table_results_view)

        self.tabWidget.addTab(self.results, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.gridLayout.addWidget(self.groupBox_2, 5, 0, 1, 1)

        self.groupBox = QGroupBox(TrainingTab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.spin_epochs = QSpinBox(self.groupBox)
        self.spin_epochs.setObjectName(u"spin_epochs")
        self.spin_epochs.setMinimumSize(QSize(110, 0))
        self.spin_epochs.setMinimum(1)
        self.spin_epochs.setMaximum(999999999)
        self.spin_epochs.setSingleStep(50)
        self.spin_epochs.setValue(100)

        self.gridLayout_2.addWidget(self.spin_epochs, 2, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 8, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(96, 0))

        self.gridLayout_2.addWidget(self.label_4, 2, 3, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(96, 0))

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(96, 0))

        self.gridLayout_2.addWidget(self.label_3, 2, 6, 1, 1)

        self.spin_batch_size = QSpinBox(self.groupBox)
        self.spin_batch_size.setObjectName(u"spin_batch_size")
        self.spin_batch_size.setMinimumSize(QSize(110, 0))
        self.spin_batch_size.setMinimum(1)
        self.spin_batch_size.setMaximum(1600)
        self.spin_batch_size.setSingleStep(8)
        self.spin_batch_size.setValue(32)

        self.gridLayout_2.addWidget(self.spin_batch_size, 2, 7, 1, 1)

        self.spin_image_size = QSpinBox(self.groupBox)
        self.spin_image_size.setObjectName(u"spin_image_size")
        self.spin_image_size.setMinimumSize(QSize(115, 0))
        self.spin_image_size.setMinimum(32)
        self.spin_image_size.setMaximum(640000)
        self.spin_image_size.setSingleStep(32)
        self.spin_image_size.setValue(640)

        self.gridLayout_2.addWidget(self.spin_image_size, 2, 1, 1, 1)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(20, 0))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line, 2, 2, 1, 1)

        self.line_5 = QFrame(self.groupBox)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMinimumSize(QSize(20, 0))
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_5, 2, 5, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)

        self.groupBox_5 = QGroupBox(TrainingTab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(96, 0))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_8, 0, 3, 1, 1)

        self.spin_freeze_layers = QSpinBox(self.groupBox_5)
        self.spin_freeze_layers.setObjectName(u"spin_freeze_layers")
        self.spin_freeze_layers.setEnabled(False)
        self.spin_freeze_layers.setMinimumSize(QSize(110, 0))
        self.spin_freeze_layers.setMaximum(99999)
        self.spin_freeze_layers.setValue(10)

        self.gridLayout_5.addWidget(self.spin_freeze_layers, 0, 4, 1, 1)

        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(96, 0))

        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)

        self.chb_transfer_learning = QCheckBox(self.groupBox_5)
        self.chb_transfer_learning.setObjectName(u"chb_transfer_learning")
        self.chb_transfer_learning.setMinimumSize(QSize(115, 0))
        self.chb_transfer_learning.setAcceptDrops(False)

        self.gridLayout_5.addWidget(self.chb_transfer_learning, 0, 1, 1, 1)

        self.line_3 = QFrame(self.groupBox_5)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(20, 0))
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_3, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 0, 5, 1, 1)


        self.gridLayout.addWidget(self.groupBox_5, 4, 0, 1, 1)

        self.groupBox_4 = QGroupBox(TrainingTab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.dspin_weight_decay = QDoubleSpinBox(self.groupBox_4)
        self.dspin_weight_decay.setObjectName(u"dspin_weight_decay")
        self.dspin_weight_decay.setMinimumSize(QSize(110, 0))
        self.dspin_weight_decay.setDecimals(4)
        self.dspin_weight_decay.setMaximum(1.000000000000000)
        self.dspin_weight_decay.setSingleStep(0.000100000000000)
        self.dspin_weight_decay.setValue(0.000500000000000)

        self.gridLayout_4.addWidget(self.dspin_weight_decay, 0, 7, 1, 1)

        self.line_2 = QFrame(self.groupBox_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(20, 0))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 0, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(96, 0))

        self.gridLayout_4.addWidget(self.label_5, 0, 3, 1, 1)

        self.cmb_optimizer = QComboBox(self.groupBox_4)
        self.cmb_optimizer.addItem("")
        self.cmb_optimizer.addItem("")
        self.cmb_optimizer.addItem("")
        self.cmb_optimizer.addItem("")
        self.cmb_optimizer.setObjectName(u"cmb_optimizer")
        self.cmb_optimizer.setMinimumSize(QSize(115, 0))

        self.gridLayout_4.addWidget(self.cmb_optimizer, 0, 1, 1, 1)

        self.dspin_initial_lr = QDoubleSpinBox(self.groupBox_4)
        self.dspin_initial_lr.setObjectName(u"dspin_initial_lr")
        self.dspin_initial_lr.setEnabled(False)
        self.dspin_initial_lr.setMinimumSize(QSize(110, 0))
        self.dspin_initial_lr.setDecimals(3)
        self.dspin_initial_lr.setMaximum(1.000000000000000)
        self.dspin_initial_lr.setSingleStep(0.000100000000000)
        self.dspin_initial_lr.setValue(0.001000000000000)

        self.gridLayout_4.addWidget(self.dspin_initial_lr, 0, 4, 1, 1)

        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(96, 0))

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 8, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(96, 0))

        self.gridLayout_4.addWidget(self.label_9, 0, 6, 1, 1)

        self.line_4 = QFrame(self.groupBox_4)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(20, 0))
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line_4, 0, 5, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 3, 0, 1, 1)

        QWidget.setTabOrder(self.cmb_selected_model, self.cmb_selected_model_type)
        QWidget.setTabOrder(self.cmb_selected_model_type, self.chb_pretrained)
        QWidget.setTabOrder(self.chb_pretrained, self.spin_image_size)
        QWidget.setTabOrder(self.spin_image_size, self.tabWidget)

        self.retranslateUi(TrainingTab)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TrainingTab)
    # setupUi

    def retranslateUi(self, TrainingTab):
        TrainingTab.setWindowTitle(QCoreApplication.translate("TrainingTab", u"Model Manager", None))
#if QT_CONFIG(tooltip)
        self.groupBox_3.setToolTip(QCoreApplication.translate("TrainingTab", u"Legt die Modellgr\u00f6\u00dfe fest", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_3.setTitle(QCoreApplication.translate("TrainingTab", u"Modellauswahl", None))
#if QT_CONFIG(tooltip)
        self.chb_pretrained.setToolTip(QCoreApplication.translate("TrainingTab", u"Nutze das am COCO Datensatz vortrainierte Modell", None))
#endif // QT_CONFIG(tooltip)
        self.chb_pretrained.setText(QCoreApplication.translate("TrainingTab", u"Vortrainiertes Modell", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("TrainingTab", u"Modellarchitektur ausw\u00e4hlen", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("TrainingTab", u"Modellarchitektur", None))
        self.lbl_model_weights.setText(QCoreApplication.translate("TrainingTab", u"keine Gewichte importiert", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("TrainingTab", u"Modellgr\u00f6", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("TrainingTab", u"Modellgr\u00f6\u00dfe", None))
#if QT_CONFIG(tooltip)
        self.label_11.setToolTip(QCoreApplication.translate("TrainingTab", u"Die Gewichte, die geladen werden sollen.", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("TrainingTab", u"Gewichte", None))
#if QT_CONFIG(tooltip)
        self.btn_import_weights.setToolTip(QCoreApplication.translate("TrainingTab", u"Auswahl der Gewichte zum importieren.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_import_weights.setText(QCoreApplication.translate("TrainingTab", u"Gewichte importieren", None))
        self.cmb_selected_model_type.setItemText(0, QCoreApplication.translate("TrainingTab", u"n", None))
        self.cmb_selected_model_type.setItemText(1, QCoreApplication.translate("TrainingTab", u"s", None))
        self.cmb_selected_model_type.setItemText(2, QCoreApplication.translate("TrainingTab", u"m", None))
        self.cmb_selected_model_type.setItemText(3, QCoreApplication.translate("TrainingTab", u"l", None))
        self.cmb_selected_model_type.setItemText(4, QCoreApplication.translate("TrainingTab", u"x", None))

        self.cmb_selected_model.setItemText(0, QCoreApplication.translate("TrainingTab", u"YOLOv12", None))

#if QT_CONFIG(tooltip)
        self.chb_resume_training.setToolTip(QCoreApplication.translate("TrainingTab", u"F\u00fchre ein unterbrochenes Training fort.\n"
"Es werden die im Modell gespeicherten Hyper-Parameter benutzt.", None))
#endif // QT_CONFIG(tooltip)
        self.chb_resume_training.setText(QCoreApplication.translate("TrainingTab", u"Training fortsetzen", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("TrainingTab", u"Modellinfo", None))
#if QT_CONFIG(tooltip)
        self.label_12.setToolTip(QCoreApplication.translate("TrainingTab", u"Bestimmt, wie viele Schichten f\u00fcr die Merkmalserkennung genutzt werden.\n"
"Wichtig f\u00fcr Transfer Learning.\n"
"Je mehr Backbone-Layer \u00fcbernommen werden, desto mehr wird bereits gelerntes Wissen genutzt.\n"
"Das ist besonders sinnvoll bei kleinen Datens\u00e4tzen.", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("TrainingTab", u"Backbone Layer", None))
        self.lbl_head_layer.setText(QCoreApplication.translate("TrainingTab", u"13", None))
        self.lbl_backbone_layer.setText(QCoreApplication.translate("TrainingTab", u"9", None))
#if QT_CONFIG(tooltip)
        self.label_14.setToolTip(QCoreApplication.translate("TrainingTab", u"Bestimmt, wie viele Schichten f\u00fcr die eigentliche Aufgabe genutzt werden\n"
"(z. B. Objekte erkennen und klassifizieren).\n"
"\n"
"Beim Transfer Learning wird der Head meist neu trainiert, um das vortrainierte Modell an den eigenen Datensatz anzupassen.\n"
"Mehr Head-Layer erm\u00f6glichen eine st\u00e4rkere Anpassung, ben\u00f6tigen aber mehr Trainingsdaten.", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("TrainingTab", u"Head Layer", None))
#if QT_CONFIG(tooltip)
        self.label_16.setToolTip(QCoreApplication.translate("TrainingTab", u"Gibt die maximale Anzahl der Schichten an, die im Modell eingefroren werden k\u00f6nnen.\n"
"Der maximale Wert entspricht der Gesamtanzahl der Schichten minus 1, damit mindestens eine Schicht trainierbar bleibt.\n"
"\n"
"Werte \u00fcber dieser Grenze werden beim Transfer Learning automatisch begrenzt.", None))
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("TrainingTab", u"Max Freeze", None))
        self.lbl_max_freeze.setText(QCoreApplication.translate("TrainingTab", u"21", None))
        self.btn_start_training.setText(QCoreApplication.translate("TrainingTab", u"Starte Training", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TrainingTab", u"Prozess", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.output), QCoreApplication.translate("TrainingTab", u"Ausgabe", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.loss), QCoreApplication.translate("TrainingTab", u"Loss", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.metric), QCoreApplication.translate("TrainingTab", u"Metrik", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.graphs), QCoreApplication.translate("TrainingTab", u"Graphen", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.results), QCoreApplication.translate("TrainingTab", u"Resultat", None))
        self.groupBox.setTitle(QCoreApplication.translate("TrainingTab", u"Parameter", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("TrainingTab", u"Anzahl der Trainingsdurchl\u00e4ufe \u00fcber den gesamten Datensatz.", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("TrainingTab", u"Epochen", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("TrainingTab", u"Die Bildaufl\u00f6sung auf denen die Trainingsbilder skaliert werden vor dem Training.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("TrainingTab", u"Bildaufl\u00f6sung", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("TrainingTab", u"Anzahl der Bilder, die gleichzeitig verarbeitet werden.\n"
"Gr\u00f6\u00dfere Batches ben\u00f6tigen mehr GPU-Speucher.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("TrainingTab", u"Batchgr\u00f6\u00dfe", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("TrainingTab", u"Transfer Learning", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("TrainingTab", u"Legt fest, wie viele Layer vom Training ausgeschlossen werden.\n"
"Werte \u00fcber der vorhandenen Layer-Anzahl werden ignoriert, d.h. der Output-Layer bleibt trainierbar.\n"
"Empfohlen: nur Backbone einfrieren.", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("TrainingTab", u"Layer einfrieren", None))
#if QT_CONFIG(tooltip)
        self.label_10.setToolTip(QCoreApplication.translate("TrainingTab", u"Transfer Learning an- oder ausschalten", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("TrainingTab", u"Modus", None))
#if QT_CONFIG(tooltip)
        self.chb_transfer_learning.setToolTip(QCoreApplication.translate("TrainingTab", u"Transfer Learning auf \"Aktiv\" stellen", None))
#endif // QT_CONFIG(tooltip)
        self.chb_transfer_learning.setText(QCoreApplication.translate("TrainingTab", u"Aktiv", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("TrainingTab", u"Optimizer", None))
#if QT_CONFIG(tooltip)
        self.dspin_weight_decay.setToolTip(QCoreApplication.translate("TrainingTab", u"L2-Regulierung zur Vermeidung von \u00dcberanpassung (Overfitting), indem gro\u00dfe Gewichte bestraft werden.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("TrainingTab", u"Schrittweite, mit der die Gewichte angepasst werden.\n"
"Zu hoch \u2192 instabil, zu niedrig \u2192 langsames Lernen.", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("TrainingTab", u"Lernrate", None))
        self.cmb_optimizer.setItemText(0, QCoreApplication.translate("TrainingTab", u"auto", None))
        self.cmb_optimizer.setItemText(1, QCoreApplication.translate("TrainingTab", u"SGD", None))
        self.cmb_optimizer.setItemText(2, QCoreApplication.translate("TrainingTab", u"Adam", None))
        self.cmb_optimizer.setItemText(3, QCoreApplication.translate("TrainingTab", u"AdamW", None))

#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("TrainingTab", u"Optimierungsverfahren zur Anpassung der Modellgewichte.\n"
"Bei \"auto\" wird automatisch der optimale Optimizer und die Lernrate ermittelt.", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("TrainingTab", u"Optimizer", None))
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("TrainingTab", u"Weight Decay ist ein Gewichtsfaktor, der gro\u00dfe Gewichte im Modell bestraft, um \u00dcberanpassung (Overfitting) zu vermeiden.", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("TrainingTab", u"Weight Decay", None))
    # retranslateUi

