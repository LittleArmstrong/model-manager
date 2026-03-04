# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_preprocessing.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPlainTextEdit, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
    QTreeView, QVBoxLayout, QWidget)

class Ui_preprocessing_tab(object):
    def setupUi(self, preprocessing_tab):
        if not preprocessing_tab.objectName():
            preprocessing_tab.setObjectName(u"preprocessing_tab")
        preprocessing_tab.resize(1263, 792)
        self.verticalLayout = QVBoxLayout(preprocessing_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabc_methods = QTabWidget(preprocessing_tab)
        self.tabc_methods.setObjectName(u"tabc_methods")
        self.tab_create_dataset = QWidget()
        self.tab_create_dataset.setObjectName(u"tab_create_dataset")
        self.verticalLayout_3 = QVBoxLayout(self.tab_create_dataset)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.tab_create_dataset)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(96, 0))

        self.horizontalLayout.addWidget(self.label_2)

        self.spin_train_split = QSpinBox(self.widget)
        self.spin_train_split.setObjectName(u"spin_train_split")
        self.spin_train_split.setMinimumSize(QSize(115, 0))
        self.spin_train_split.setValue(70)

        self.horizontalLayout.addWidget(self.spin_train_split)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addWidget(self.widget)

        self.widget_2 = QWidget(self.groupBox)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(96, 0))

        self.horizontalLayout_2.addWidget(self.label_3)

        self.spin_val_split = QSpinBox(self.widget_2)
        self.spin_val_split.setObjectName(u"spin_val_split")
        self.spin_val_split.setMinimumSize(QSize(115, 0))
        self.spin_val_split.setValue(20)

        self.horizontalLayout_2.addWidget(self.spin_val_split)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.groupBox)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(96, 0))

        self.horizontalLayout_3.addWidget(self.label_4)

        self.spin_test_split = QSpinBox(self.widget_3)
        self.spin_test_split.setObjectName(u"spin_test_split")
        self.spin_test_split.setMinimumSize(QSize(115, 0))
        self.spin_test_split.setValue(10)

        self.horizontalLayout_3.addWidget(self.spin_test_split)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addWidget(self.widget_3)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab_create_dataset)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_4 = QWidget(self.groupBox_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(96, 0))

        self.horizontalLayout_4.addWidget(self.label_5)

        self.spin_img_size = QSpinBox(self.widget_4)
        self.spin_img_size.setObjectName(u"spin_img_size")
        self.spin_img_size.setMinimumSize(QSize(115, 0))
        self.spin_img_size.setMaximum(999999999)
        self.spin_img_size.setValue(640)

        self.horizontalLayout_4.addWidget(self.spin_img_size)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addWidget(self.widget_4)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_5 = QGroupBox(self.tab_create_dataset)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(18, -1, -1, -1)
        self.label = QLabel(self.groupBox_5)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(96, 0))

        self.horizontalLayout_7.addWidget(self.label)

        self.le_class_names = QLineEdit(self.groupBox_5)
        self.le_class_names.setObjectName(u"le_class_names")

        self.horizontalLayout_7.addWidget(self.le_class_names)


        self.verticalLayout_3.addWidget(self.groupBox_5)

        self.groupBox_3 = QGroupBox(self.tab_create_dataset)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout = QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_11 = QWidget(self.groupBox_3)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.gridLayout.addWidget(self.widget_11, 0, 3, 1, 1)

        self.le_create_dataset_path = QLineEdit(self.groupBox_3)
        self.le_create_dataset_path.setObjectName(u"le_create_dataset_path")
        self.le_create_dataset_path.setMinimumSize(QSize(435, 0))
        font = QFont()
        font.setItalic(True)
        self.le_create_dataset_path.setFont(font)
        self.le_create_dataset_path.setReadOnly(True)

        self.gridLayout.addWidget(self.le_create_dataset_path, 0, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(96, 0))

        self.gridLayout.addWidget(self.label_15, 1, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(96, 0))

        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)

        self.btn_create_dataset_path = QPushButton(self.groupBox_3)
        self.btn_create_dataset_path.setObjectName(u"btn_create_dataset_path")

        self.gridLayout.addWidget(self.btn_create_dataset_path, 0, 2, 1, 1)

        self.le_dataset_name = QLineEdit(self.groupBox_3)
        self.le_dataset_name.setObjectName(u"le_dataset_name")

        self.gridLayout.addWidget(self.le_dataset_name, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pb_creation_progress = QProgressBar(self.tab_create_dataset)
        self.pb_creation_progress.setObjectName(u"pb_creation_progress")
        self.pb_creation_progress.setValue(0)

        self.verticalLayout_3.addWidget(self.pb_creation_progress)

        self.btn_create_dataset = QPushButton(self.tab_create_dataset)
        self.btn_create_dataset.setObjectName(u"btn_create_dataset")

        self.verticalLayout_3.addWidget(self.btn_create_dataset)

        self.tabc_methods.addTab(self.tab_create_dataset, "")
        self.tab_augment_dataset = QWidget()
        self.tab_augment_dataset.setObjectName(u"tab_augment_dataset")
        self.verticalLayout_2 = QVBoxLayout(self.tab_augment_dataset)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_4 = QGroupBox(self.tab_augment_dataset)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_6 = QWidget(self.groupBox_4)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.widget_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(96, 0))

        self.horizontalLayout_8.addWidget(self.label_7)

        self.spin_rotation = QSpinBox(self.widget_6)
        self.spin_rotation.setObjectName(u"spin_rotation")
        self.spin_rotation.setMinimumSize(QSize(100, 0))
        self.spin_rotation.setMaximum(360)
        self.spin_rotation.setValue(15)

        self.horizontalLayout_8.addWidget(self.spin_rotation)

        self.line = QFrame(self.widget_6)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(20, 0))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line)

        self.label_8 = QLabel(self.widget_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(96, 0))
        self.label_8.setIndent(0)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.dspin_translation = QDoubleSpinBox(self.widget_6)
        self.dspin_translation.setObjectName(u"dspin_translation")
        self.dspin_translation.setMinimumSize(QSize(100, 0))
        self.dspin_translation.setMaximum(1.000000000000000)
        self.dspin_translation.setValue(0.100000000000000)

        self.horizontalLayout_8.addWidget(self.dspin_translation)

        self.line_3 = QFrame(self.widget_6)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(20, 0))
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_3)

        self.label_10 = QLabel(self.widget_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(96, 0))

        self.horizontalLayout_8.addWidget(self.label_10)

        self.dspin_zoom = QDoubleSpinBox(self.widget_6)
        self.dspin_zoom.setObjectName(u"dspin_zoom")
        self.dspin_zoom.setMinimumSize(QSize(100, 0))
        self.dspin_zoom.setMaximum(1.000000000000000)
        self.dspin_zoom.setValue(0.100000000000000)

        self.horizontalLayout_8.addWidget(self.dspin_zoom)

        self.line_6 = QFrame(self.widget_6)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_6)

        self.label_6 = QLabel(self.widget_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(96, 0))

        self.horizontalLayout_8.addWidget(self.label_6)

        self.dspin_flip_lr = QDoubleSpinBox(self.widget_6)
        self.dspin_flip_lr.setObjectName(u"dspin_flip_lr")
        self.dspin_flip_lr.setMinimumSize(QSize(100, 0))
        self.dspin_flip_lr.setMaximum(1.000000000000000)
        self.dspin_flip_lr.setSingleStep(0.010000000000000)

        self.horizontalLayout_8.addWidget(self.dspin_flip_lr)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addWidget(self.widget_6)

        self.line_5 = QFrame(self.groupBox_4)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_5)

        self.widget_8 = QWidget(self.groupBox_4)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(20, 0))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_13 = QLabel(self.widget_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(96, 0))

        self.horizontalLayout_10.addWidget(self.label_13)

        self.dspin_noise = QDoubleSpinBox(self.widget_8)
        self.dspin_noise.setObjectName(u"dspin_noise")
        self.dspin_noise.setMinimumSize(QSize(100, 0))
        self.dspin_noise.setMaximum(1.000000000000000)
        self.dspin_noise.setValue(0.100000000000000)

        self.horizontalLayout_10.addWidget(self.dspin_noise)

        self.line_2 = QFrame(self.widget_8)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(20, 0))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_10.addWidget(self.line_2)

        self.label_9 = QLabel(self.widget_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(96, 0))
        self.label_9.setIndent(0)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.dspin_contrast = QDoubleSpinBox(self.widget_8)
        self.dspin_contrast.setObjectName(u"dspin_contrast")
        self.dspin_contrast.setMinimumSize(QSize(100, 0))
        self.dspin_contrast.setMaximum(1.000000000000000)
        self.dspin_contrast.setValue(0.100000000000000)

        self.horizontalLayout_10.addWidget(self.dspin_contrast)

        self.line_4 = QFrame(self.widget_8)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(20, 0))
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_10.addWidget(self.line_4)

        self.label_11 = QLabel(self.widget_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(96, 0))

        self.horizontalLayout_10.addWidget(self.label_11)

        self.dspin_brightness = QDoubleSpinBox(self.widget_8)
        self.dspin_brightness.setObjectName(u"dspin_brightness")
        self.dspin_brightness.setMinimumSize(QSize(100, 0))
        self.dspin_brightness.setMaximum(1.000000000000000)
        self.dspin_brightness.setValue(0.100000000000000)

        self.horizontalLayout_10.addWidget(self.dspin_brightness)

        self.line_7 = QFrame(self.widget_8)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_10.addWidget(self.line_7)

        self.label_18 = QLabel(self.widget_8)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(96, 0))

        self.horizontalLayout_10.addWidget(self.label_18)

        self.dspin_flip_ud = QDoubleSpinBox(self.widget_8)
        self.dspin_flip_ud.setObjectName(u"dspin_flip_ud")
        self.dspin_flip_ud.setMinimumSize(QSize(100, 0))
        self.dspin_flip_ud.setMaximum(1.000000000000000)
        self.dspin_flip_ud.setSingleStep(0.010000000000000)

        self.horizontalLayout_10.addWidget(self.dspin_flip_ud)

        self.horizontalSpacer_7 = QSpacerItem(830, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)


        self.verticalLayout_6.addWidget(self.widget_8)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_7 = QGroupBox(self.tab_augment_dataset)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(100, 0))
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_15 = QWidget(self.groupBox_7)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_12 = QLabel(self.widget_15)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(96, 0))

        self.horizontalLayout_15.addWidget(self.label_12)

        self.spin_num_per_img = QSpinBox(self.widget_15)
        self.spin_num_per_img.setObjectName(u"spin_num_per_img")
        self.spin_num_per_img.setMinimumSize(QSize(100, 0))
        self.spin_num_per_img.setValue(3)

        self.horizontalLayout_15.addWidget(self.spin_num_per_img)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_11)


        self.verticalLayout_11.addWidget(self.widget_15)


        self.verticalLayout_2.addWidget(self.groupBox_7)

        self.groupBox_6 = QGroupBox(self.tab_augment_dataset)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_2 = QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 0, 4, 1, 1)

        self.label_16 = QLabel(self.groupBox_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(96, 0))

        self.gridLayout_2.addWidget(self.label_16, 0, 0, 1, 1)

        self.le_augment_dataset_path = QLineEdit(self.groupBox_6)
        self.le_augment_dataset_path.setObjectName(u"le_augment_dataset_path")
        self.le_augment_dataset_path.setMinimumSize(QSize(435, 22))
        self.le_augment_dataset_path.setFont(font)
        self.le_augment_dataset_path.setReadOnly(True)

        self.gridLayout_2.addWidget(self.le_augment_dataset_path, 0, 2, 1, 1)

        self.le_augmented_dataset_name = QLineEdit(self.groupBox_6)
        self.le_augmented_dataset_name.setObjectName(u"le_augmented_dataset_name")
        self.le_augmented_dataset_name.setMinimumSize(QSize(0, 22))

        self.gridLayout_2.addWidget(self.le_augmented_dataset_name, 1, 2, 1, 1)

        self.btn_augment_dataset_path = QPushButton(self.groupBox_6)
        self.btn_augment_dataset_path.setObjectName(u"btn_augment_dataset_path")

        self.gridLayout_2.addWidget(self.btn_augment_dataset_path, 0, 3, 1, 1)

        self.label_17 = QLabel(self.groupBox_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(96, 0))

        self.gridLayout_2.addWidget(self.label_17, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_6)

        self.groupBox_8 = QGroupBox(self.tab_augment_dataset)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.pte_augment_output = QPlainTextEdit(self.groupBox_8)
        self.pte_augment_output.setObjectName(u"pte_augment_output")

        self.verticalLayout_12.addWidget(self.pte_augment_output)


        self.verticalLayout_2.addWidget(self.groupBox_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.pb_augment_progress = QProgressBar(self.tab_augment_dataset)
        self.pb_augment_progress.setObjectName(u"pb_augment_progress")
        self.pb_augment_progress.setValue(0)

        self.verticalLayout_2.addWidget(self.pb_augment_progress)

        self.btn_augment_dataset = QPushButton(self.tab_augment_dataset)
        self.btn_augment_dataset.setObjectName(u"btn_augment_dataset")

        self.verticalLayout_2.addWidget(self.btn_augment_dataset)

        self.tabc_methods.addTab(self.tab_augment_dataset, "")
        self.tab_preview = QWidget()
        self.tab_preview.setObjectName(u"tab_preview")
        self.verticalLayout_7 = QVBoxLayout(self.tab_preview)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_9 = QWidget(self.tab_preview)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tv_dataset = QTreeView(self.widget_9)
        self.tv_dataset.setObjectName(u"tv_dataset")

        self.horizontalLayout_13.addWidget(self.tv_dataset)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_10)

        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_8 = QVBoxLayout(self.widget_10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.lbl_img = QLabel(self.widget_10)
        self.lbl_img.setObjectName(u"lbl_img")
        self.lbl_img.setMinimumSize(QSize(640, 640))
        self.lbl_img.setMaximumSize(QSize(640, 640))

        self.verticalLayout_8.addWidget(self.lbl_img)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)


        self.horizontalLayout_13.addWidget(self.widget_10)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)


        self.verticalLayout_7.addWidget(self.widget_9)

        self.btn_load_dataset_preview = QPushButton(self.tab_preview)
        self.btn_load_dataset_preview.setObjectName(u"btn_load_dataset_preview")

        self.verticalLayout_7.addWidget(self.btn_load_dataset_preview)

        self.tabc_methods.addTab(self.tab_preview, "")

        self.verticalLayout.addWidget(self.tabc_methods)


        self.retranslateUi(preprocessing_tab)

        self.tabc_methods.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(preprocessing_tab)
    # setupUi

    def retranslateUi(self, preprocessing_tab):
        preprocessing_tab.setWindowTitle(QCoreApplication.translate("preprocessing_tab", u"Model Manager", None))
        self.groupBox.setTitle(QCoreApplication.translate("preprocessing_tab", u"Datensatz Split", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("preprocessing_tab", u"Anzahl der Bilder im Trainings-Split.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("preprocessing_tab", u"Training %:", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("preprocessing_tab", u"Anzahl der Bilder im Validierungs-Split.", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("preprocessing_tab", u"Validierung %:", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("preprocessing_tab", u"Anzahl der Bilder im Test-Split.", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("preprocessing_tab", u"Test %:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("preprocessing_tab", u"Bild", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("preprocessing_tab", u"Die Bildaufl\u00f6sung, auf denen die Bilder skaliert werden.", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("preprocessing_tab", u"Aufl\u00f6sung (px)", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("preprocessing_tab", u"Metadaten", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("preprocessing_tab", u"Die Namen der Klassen, die im Modell trainiert werden sollen.\n"
"Die Reihenfolge bestimmt den Klassenindex, der bei den Labels benutzt wird.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("preprocessing_tab", u"Klassennamen", None))
        self.le_class_names.setPlaceholderText(QCoreApplication.translate("preprocessing_tab", u"Klasse1, Klasse2", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("preprocessing_tab", u"Speicherort", None))
        self.le_create_dataset_path.setText("")
        self.le_create_dataset_path.setPlaceholderText(QCoreApplication.translate("preprocessing_tab", u"kein Speicherort ausgew\u00e4hlt", None))
#if QT_CONFIG(tooltip)
        self.label_15.setToolTip(QCoreApplication.translate("preprocessing_tab", u"Der Name mit dem dieser Datensatz gespeichert werden soll", None))
#endif // QT_CONFIG(tooltip)
        self.label_15.setText(QCoreApplication.translate("preprocessing_tab", u"Datensatzname", None))
#if QT_CONFIG(tooltip)
        self.label_14.setToolTip(QCoreApplication.translate("preprocessing_tab", u"Der Ordner in dem der Datensatz gespeichert werden soll.\n"
"Wenn nicht angegeben, dann wird dort gespeichert, wo die Anwendung gestartet wurde.", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("preprocessing_tab", u"Ordner", None))
        self.btn_create_dataset_path.setText(QCoreApplication.translate("preprocessing_tab", u"Speicherort ausw\u00e4hlen", None))
        self.le_dataset_name.setText(QCoreApplication.translate("preprocessing_tab", u"Datensatz", None))
        self.btn_create_dataset.setText(QCoreApplication.translate("preprocessing_tab", u"Datensatz erstellen", None))
        self.tabc_methods.setTabText(self.tabc_methods.indexOf(self.tab_create_dataset), QCoreApplication.translate("preprocessing_tab", u"Datensatz erstellen", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("preprocessing_tab", u"Augmentierungsmethoden", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("preprocessing_tab", u"Rotation (Grad)", None))
        self.label_8.setText(QCoreApplication.translate("preprocessing_tab", u"Translation", None))
        self.label_10.setText(QCoreApplication.translate("preprocessing_tab", u"Zoom", None))
        self.label_6.setText(QCoreApplication.translate("preprocessing_tab", u"Flip Horizontal", None))
        self.label_13.setText(QCoreApplication.translate("preprocessing_tab", u"Rauschen", None))
        self.label_9.setText(QCoreApplication.translate("preprocessing_tab", u"Kontrast", None))
        self.label_11.setText(QCoreApplication.translate("preprocessing_tab", u"Helligkeit", None))
        self.label_18.setText(QCoreApplication.translate("preprocessing_tab", u"Flip Vertikal", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("preprocessing_tab", u"H\u00e4ufigkeit", None))
        self.label_12.setText(QCoreApplication.translate("preprocessing_tab", u"Anzahl pro Bild", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("preprocessing_tab", u"Speicherort", None))
        self.label_16.setText(QCoreApplication.translate("preprocessing_tab", u"Ordner", None))
        self.le_augment_dataset_path.setPlaceholderText(QCoreApplication.translate("preprocessing_tab", u"kein Speicherort ausgew\u00e4hlt", None))
        self.le_augmented_dataset_name.setText(QCoreApplication.translate("preprocessing_tab", u"Datensatz_Augmentiert", None))
        self.btn_augment_dataset_path.setText(QCoreApplication.translate("preprocessing_tab", u"Speicherort ausw\u00e4hlen", None))
        self.label_17.setText(QCoreApplication.translate("preprocessing_tab", u"Datensatzname", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("preprocessing_tab", u"Ausgabe", None))
        self.btn_augment_dataset.setText(QCoreApplication.translate("preprocessing_tab", u"Datensatz augmentieren", None))
        self.tabc_methods.setTabText(self.tabc_methods.indexOf(self.tab_augment_dataset), QCoreApplication.translate("preprocessing_tab", u"Datensatz augmentieren", None))
        self.lbl_img.setText("")
        self.btn_load_dataset_preview.setText(QCoreApplication.translate("preprocessing_tab", u"Datensatz laden", None))
        self.tabc_methods.setTabText(self.tabc_methods.indexOf(self.tab_preview), QCoreApplication.translate("preprocessing_tab", u"Vorschau", None))
    # retranslateUi

