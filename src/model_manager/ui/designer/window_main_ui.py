# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_main.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1492, 1097)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(32)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_selected_dataset = QLabel(self.widget)
        self.lbl_selected_dataset.setObjectName(u"lbl_selected_dataset")
        self.lbl_selected_dataset.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.lbl_selected_dataset)

        self.btn_select_dataset = QPushButton(self.widget)
        self.btn_select_dataset.setObjectName(u"btn_select_dataset")
        self.btn_select_dataset.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.btn_select_dataset)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout.addWidget(self.groupBox)

        self.tabc_main = QTabWidget(self.centralwidget)
        self.tabc_main.setObjectName(u"tabc_main")

        self.verticalLayout.addWidget(self.tabc_main)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1492, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabc_main.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Model  Manager", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Datensatz", None))
        self.lbl_selected_dataset.setText(QCoreApplication.translate("MainWindow", u"kein Datensatz ausgew\u00e4hlt", None))
        self.btn_select_dataset.setText(QCoreApplication.translate("MainWindow", u"Datensatz ausw\u00e4hlen", None))
    # retranslateUi

