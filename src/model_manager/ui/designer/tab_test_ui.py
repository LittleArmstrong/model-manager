# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_test.ui'
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
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QProgressBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

class Ui_TestTab(object):
    def setupUi(self, TestTab):
        if not TestTab.objectName():
            TestTab.setObjectName(u"TestTab")
        TestTab.resize(1232, 1192)
        self.verticalLayout = QVBoxLayout(TestTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.model_container = QGroupBox(TestTab)
        self.model_container.setObjectName(u"model_container")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.model_container.setFont(font)
        self.gridLayout_2 = QGridLayout(self.model_container)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_model_weights = QLabel(self.model_container)
        self.lbl_model_weights.setObjectName(u"lbl_model_weights")
        self.lbl_model_weights.setEnabled(False)
        self.lbl_model_weights.setMinimumSize(QSize(150, 0))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(True)
        font1.setKerning(True)
        self.lbl_model_weights.setFont(font1)
        self.lbl_model_weights.setMargin(5)

        self.gridLayout_2.addWidget(self.lbl_model_weights, 3, 3, 2, 1)

        self.btn_import_weights = QPushButton(self.model_container)
        self.btn_import_weights.setObjectName(u"btn_import_weights")
        self.btn_import_weights.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_import_weights.sizePolicy().hasHeightForWidth())
        self.btn_import_weights.setSizePolicy(sizePolicy)
        self.btn_import_weights.setMaximumSize(QSize(160, 16777215))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(False)
        self.btn_import_weights.setFont(font2)

        self.gridLayout_2.addWidget(self.btn_import_weights, 3, 4, 2, 1)

        self.label_2 = QLabel(self.model_container)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setFont(font2)
        self.label_2.setMargin(1)

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.cmb_selected_model = QComboBox(self.model_container)
        self.cmb_selected_model.setObjectName(u"cmb_selected_model")
        self.cmb_selected_model.setEnabled(False)
        self.cmb_selected_model.setMinimumSize(QSize(150, 0))
        self.cmb_selected_model.setFont(font2)

        self.gridLayout_2.addWidget(self.cmb_selected_model, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 4, 3, 1)

        self.line = QFrame(self.model_container)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line, 3, 2, 2, 1)

        self.chb_last_model = QCheckBox(self.model_container)
        self.chb_last_model.setObjectName(u"chb_last_model")
        self.chb_last_model.setFont(font2)
        self.chb_last_model.setChecked(True)

        self.gridLayout_2.addWidget(self.chb_last_model, 4, 1, 1, 1)

        self.label_3 = QLabel(self.model_container)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setFont(font2)
        self.label_3.setMargin(1)

        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)

        self.cmb_selected_size = QComboBox(self.model_container)
        self.cmb_selected_size.setObjectName(u"cmb_selected_size")
        self.cmb_selected_size.setEnabled(False)
        self.cmb_selected_size.setMinimumSize(QSize(150, 0))
        self.cmb_selected_size.setFont(font2)

        self.gridLayout_2.addWidget(self.cmb_selected_size, 1, 3, 1, 1)


        self.verticalLayout.addWidget(self.model_container)

        self.groupBox = QGroupBox(TestTab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setFont(font2)
        self.label_4.setMargin(0)
        self.label_4.setIndent(0)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)

        self.spin_batch_size = QSpinBox(self.groupBox)
        self.spin_batch_size.setObjectName(u"spin_batch_size")
        self.spin_batch_size.setMinimumSize(QSize(100, 0))
        self.spin_batch_size.setFont(font2)
        self.spin_batch_size.setMinimum(1)
        self.spin_batch_size.setMaximum(9999)
        self.spin_batch_size.setValue(16)

        self.gridLayout.addWidget(self.spin_batch_size, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(TestTab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 0))
        self.label_6.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.dspin_min_score = QDoubleSpinBox(self.groupBox_2)
        self.dspin_min_score.setObjectName(u"dspin_min_score")
        self.dspin_min_score.setMinimumSize(QSize(100, 0))
        self.dspin_min_score.setFont(font2)
        self.dspin_min_score.setMaximum(100.000000000000000)
        self.dspin_min_score.setValue(25.000000000000000)

        self.horizontalLayout_2.addWidget(self.dspin_min_score)

        self.horizontalSpacer_9 = QSpacerItem(30, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 0))
        self.label_7.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.dspin_min_nms_iou = QDoubleSpinBox(self.groupBox_2)
        self.dspin_min_nms_iou.setObjectName(u"dspin_min_nms_iou")
        self.dspin_min_nms_iou.setMinimumSize(QSize(100, 0))
        self.dspin_min_nms_iou.setFont(font2)
        self.dspin_min_nms_iou.setMaximum(100.000000000000000)
        self.dspin_min_nms_iou.setSingleStep(1.000000000000000)
        self.dspin_min_nms_iou.setValue(70.000000000000000)

        self.horizontalLayout_2.addWidget(self.dspin_min_nms_iou)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.preview_container = QGroupBox(TestTab)
        self.preview_container.setObjectName(u"preview_container")
        self.preview_container.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.preview_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabc_test = QTabWidget(self.preview_container)
        self.tabc_test.setObjectName(u"tabc_test")
        self.tabc_test.setFont(font2)
        self.tab_preview = QWidget()
        self.tab_preview.setObjectName(u"tab_preview")
        self.verticalLayout_5 = QVBoxLayout(self.tab_preview)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.tab_preview)
        self.widget.setObjectName(u"widget")
        self.widget.setFont(font2)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.cmb_sort_order = QComboBox(self.widget)
        self.cmb_sort_order.addItem("")
        self.cmb_sort_order.addItem("")
        self.cmb_sort_order.addItem("")
        self.cmb_sort_order.setObjectName(u"cmb_sort_order")

        self.horizontalLayout.addWidget(self.cmb_sort_order)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addWidget(self.widget)

        self.widget_2 = QWidget(self.tab_preview)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setFont(font2)
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_prev_img = QPushButton(self.widget_2)
        self.btn_prev_img.setObjectName(u"btn_prev_img")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_prev_img.sizePolicy().hasHeightForWidth())
        self.btn_prev_img.setSizePolicy(sizePolicy1)
        self.btn_prev_img.setMinimumSize(QSize(70, 70))
        self.btn_prev_img.setMaximumSize(QSize(70, 9999999))
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(False)
        self.btn_prev_img.setFont(font3)
        self.btn_prev_img.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_prev_img.setCheckable(False)
        self.btn_prev_img.setAutoDefault(False)
        self.btn_prev_img.setFlat(True)

        self.gridLayout_3.addWidget(self.btn_prev_img, 0, 1, 1, 1)

        self.scrollArea = QScrollArea(self.widget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 652, 649))
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.img_preview = QLabel(self.scrollAreaWidgetContents_3)
        self.img_preview.setObjectName(u"img_preview")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.img_preview.sizePolicy().hasHeightForWidth())
        self.img_preview.setSizePolicy(sizePolicy2)
        self.img_preview.setMinimumSize(QSize(640, 640))
        self.img_preview.setMaximumSize(QSize(640, 640))
        self.img_preview.setScaledContents(True)
        self.img_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.img_preview)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_3.addWidget(self.scrollArea, 0, 3, 1, 1)

        self.btn_next_img = QPushButton(self.widget_2)
        self.btn_next_img.setObjectName(u"btn_next_img")
        sizePolicy1.setHeightForWidth(self.btn_next_img.sizePolicy().hasHeightForWidth())
        self.btn_next_img.setSizePolicy(sizePolicy1)
        self.btn_next_img.setMinimumSize(QSize(70, 70))
        self.btn_next_img.setMaximumSize(QSize(70, 16777215))
        self.btn_next_img.setFont(font3)
        self.btn_next_img.setFlat(True)

        self.gridLayout_3.addWidget(self.btn_next_img, 0, 5, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 4, 1, 1)


        self.verticalLayout_5.addWidget(self.widget_2)

        self.tabc_test.addTab(self.tab_preview, "")
        self.tab_results = QWidget()
        self.tab_results.setObjectName(u"tab_results")
        self.verticalLayout_6 = QVBoxLayout(self.tab_results)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.table_results_view = QTableView(self.tab_results)
        self.table_results_view.setObjectName(u"table_results_view")
        self.table_results_view.horizontalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_6.addWidget(self.table_results_view)

        self.tabc_test.addTab(self.tab_results, "")

        self.verticalLayout_3.addWidget(self.tabc_test)


        self.verticalLayout.addWidget(self.preview_container)

        self.pb_progress_bar = QProgressBar(TestTab)
        self.pb_progress_bar.setObjectName(u"pb_progress_bar")
        self.pb_progress_bar.setValue(0)

        self.verticalLayout.addWidget(self.pb_progress_bar)

        self.btn_start_testing = QPushButton(TestTab)
        self.btn_start_testing.setObjectName(u"btn_start_testing")
        font4 = QFont()
        font4.setPointSize(9)
        self.btn_start_testing.setFont(font4)

        self.verticalLayout.addWidget(self.btn_start_testing)

        QWidget.setTabOrder(self.cmb_selected_model, self.chb_last_model)
        QWidget.setTabOrder(self.chb_last_model, self.btn_import_weights)
        QWidget.setTabOrder(self.btn_import_weights, self.spin_batch_size)
        QWidget.setTabOrder(self.spin_batch_size, self.btn_start_testing)
        QWidget.setTabOrder(self.btn_start_testing, self.tabc_test)
        QWidget.setTabOrder(self.tabc_test, self.cmb_sort_order)
        QWidget.setTabOrder(self.cmb_sort_order, self.btn_prev_img)
        QWidget.setTabOrder(self.btn_prev_img, self.btn_next_img)
        QWidget.setTabOrder(self.btn_next_img, self.table_results_view)

        self.retranslateUi(TestTab)

        self.tabc_test.setCurrentIndex(0)
        self.btn_prev_img.setDefault(False)
        self.btn_next_img.setDefault(False)


        QMetaObject.connectSlotsByName(TestTab)
    # setupUi

    def retranslateUi(self, TestTab):
        TestTab.setWindowTitle(QCoreApplication.translate("TestTab", u"Model Manager", None))
        self.model_container.setTitle(QCoreApplication.translate("TestTab", u"Modell", None))
        self.lbl_model_weights.setText(QCoreApplication.translate("TestTab", u"keine Gewichte importiert", None))
#if QT_CONFIG(tooltip)
        self.btn_import_weights.setToolTip(QCoreApplication.translate("TestTab", u"Importiert vortrainierte Modellgewichte f\u00fcr den Test.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_import_weights.setText(QCoreApplication.translate("TestTab", u"Gewichte importieren", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("TestTab", u"Auswahl der Modellarchitektur des zu testenden Modells.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("TestTab", u"Modellarchitektur", None))
#if QT_CONFIG(tooltip)
        self.chb_last_model.setToolTip(QCoreApplication.translate("TestTab", u"Verwendet das zuletzt trainierte Modell f\u00fcr den Test.\n"
"\n"
"Falls deaktiviert, werden die ausgew\u00e4hlten Gewichte verwendet.", None))
#endif // QT_CONFIG(tooltip)
        self.chb_last_model.setText(QCoreApplication.translate("TestTab", u"letztes Modell", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("TestTab", u"Auswahl der Modellarchitektur des zu testenden Modells.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("TestTab", u"Modellgr\u00f6\u00dfe", None))
        self.groupBox.setTitle(QCoreApplication.translate("TestTab", u"Bildparameter", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("TestTab", u"Anzahl der Bilder pro Testschritt.", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("TestTab", u"Batchgr\u00f6\u00dfe", None))
#if QT_CONFIG(tooltip)
        self.spin_batch_size.setToolTip(QCoreApplication.translate("TestTab", u"Anzahl der Bilder pro Testschritt (Batch Size).", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("TestTab", u"Vorhersageparameter", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("TestTab", u"Mindest-Konfidenz (%) f\u00fcr die Anzeige von Vorhersagen", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("TestTab", u"Min Score (%)", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("TestTab", u"IoU\u2011Schwelle (%) f\u00fcr die Non\u2011Maximum Suppression:\n"
"Boxen mit einer \u00dcberlappung \u00fcber diesem Wert werden als Duplikate entfernt.", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("TestTab", u"Erlaubte \u00dcberdeckung (%)", None))
        self.preview_container.setTitle(QCoreApplication.translate("TestTab", u"Ausgabe", None))
        self.label.setText(QCoreApplication.translate("TestTab", u"Sortierung:", None))
        self.cmb_sort_order.setItemText(0, QCoreApplication.translate("TestTab", u"Original", None))
        self.cmb_sort_order.setItemText(1, QCoreApplication.translate("TestTab", u"Score aufsteigend", None))
        self.cmb_sort_order.setItemText(2, QCoreApplication.translate("TestTab", u"Score absteigend", None))

        self.btn_prev_img.setText(QCoreApplication.translate("TestTab", u"<", None))
        self.img_preview.setText("")
        self.btn_next_img.setText(QCoreApplication.translate("TestTab", u">", None))
        self.tabc_test.setTabText(self.tabc_test.indexOf(self.tab_preview), QCoreApplication.translate("TestTab", u"Vorschau", None))
        self.tabc_test.setTabText(self.tabc_test.indexOf(self.tab_results), QCoreApplication.translate("TestTab", u"Resultat", None))
#if QT_CONFIG(tooltip)
        self.btn_start_testing.setToolTip(QCoreApplication.translate("TestTab", u"Testet die Modellleistung am ausgew\u00e4hlten Datensatz.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_start_testing.setText(QCoreApplication.translate("TestTab", u"Starte Test", None))
    # retranslateUi

