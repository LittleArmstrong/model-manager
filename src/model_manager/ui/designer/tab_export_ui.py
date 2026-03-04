# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_export.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_ExportTab(object):
    def setupUi(self, ExportTab):
        if not ExportTab.objectName():
            ExportTab.setObjectName(u"ExportTab")
        ExportTab.resize(1232, 1186)
        self.verticalLayout = QVBoxLayout(ExportTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.model_container = QGroupBox(ExportTab)
        self.model_container.setObjectName(u"model_container")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.model_container.setFont(font)
        self.gridLayout_2 = QGridLayout(self.model_container)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(30)
        self.label_3 = QLabel(self.model_container)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        self.label_3.setFont(font1)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.btn_model_export = QPushButton(self.model_container)
        self.btn_model_export.setObjectName(u"btn_model_export")
        self.btn_model_export.setEnabled(False)
        self.btn_model_export.setMinimumSize(QSize(150, 32))
        self.btn_model_export.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_model_export, 0, 2, 1, 1)

        self.lbl_model_path = QLabel(self.model_container)
        self.lbl_model_path.setObjectName(u"lbl_model_path")
        self.lbl_model_path.setMinimumSize(QSize(350, 0))
        self.lbl_model_path.setFont(font1)

        self.gridLayout_2.addWidget(self.lbl_model_path, 0, 1, 1, 1)

        self.btn_code_export = QPushButton(self.model_container)
        self.btn_code_export.setObjectName(u"btn_code_export")
        self.btn_code_export.setMinimumSize(QSize(150, 32))
        self.btn_code_export.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_code_export, 2, 2, 1, 1)

        self.label_2 = QLabel(self.model_container)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.lineEdit = QLineEdit(self.model_container)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(100, 0))
        self.lineEdit.setFont(font1)

        self.gridLayout_2.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.label_4 = QLabel(self.model_container)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.lbl_model_path_last = QLabel(self.model_container)
        self.lbl_model_path_last.setObjectName(u"lbl_model_path_last")
        self.lbl_model_path_last.setFont(font1)

        self.gridLayout_2.addWidget(self.lbl_model_path_last, 1, 1, 1, 1)

        self.btn_model_last_export = QPushButton(self.model_container)
        self.btn_model_last_export.setObjectName(u"btn_model_last_export")
        self.btn_model_last_export.setEnabled(False)
        self.btn_model_last_export.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_model_last_export, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.model_container)

        self.groupBox = QGroupBox(ExportTab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(13)
        self.lbl_train_seed = QLabel(self.groupBox)
        self.lbl_train_seed.setObjectName(u"lbl_train_seed")

        self.gridLayout.addWidget(self.lbl_train_seed, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(ExportTab)

        QMetaObject.connectSlotsByName(ExportTab)
    # setupUi

    def retranslateUi(self, ExportTab):
        ExportTab.setWindowTitle(QCoreApplication.translate("ExportTab", u"Model Manager", None))
        self.model_container.setTitle(QCoreApplication.translate("ExportTab", u"Export", None))
        self.label_3.setText(QCoreApplication.translate("ExportTab", u"Modellpfad (beste Epoche)", None))
        self.btn_model_export.setText(QCoreApplication.translate("ExportTab", u"Exportiere Modell", None))
#if QT_CONFIG(tooltip)
        self.lbl_model_path.setToolTip(QCoreApplication.translate("ExportTab", u"Interner Pfad des zuletzt trainierten Modells", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lbl_model_path.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.lbl_model_path.setText(QCoreApplication.translate("ExportTab", u"Modellpfad", None))
        self.btn_code_export.setText(QCoreApplication.translate("ExportTab", u"Exportiere Code Vorlage", None))
        self.label_2.setText(QCoreApplication.translate("ExportTab", u"Ordnername", None))
        self.lineEdit.setText(QCoreApplication.translate("ExportTab", u"Code_Export", None))
        self.lineEdit.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("ExportTab", u"Modellpfad (letzte Epoche)", None))
        self.lbl_model_path_last.setText(QCoreApplication.translate("ExportTab", u"Modellpfad", None))
        self.btn_model_last_export.setText(QCoreApplication.translate("ExportTab", u"Exportiere Modell", None))
        self.groupBox.setTitle(QCoreApplication.translate("ExportTab", u"Info", None))
        self.lbl_train_seed.setText(QCoreApplication.translate("ExportTab", u"seed", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("ExportTab", u"Fester Ausgangswert zum Ausrechnen von Zufallszahlen, um das Training reproduzierbar zu machen.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label.setText(QCoreApplication.translate("ExportTab", u"Trainings-Seed:", None))
    # retranslateUi

