# -*- coding: utf-8 -*-
import qdarkstyle
################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QMainWindow, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 519)
        MainWindow.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='PySide6'))
#         MainWindow.setStyleSheet(u"/*\n"
# "	Copyright 2013 Emanuel Claesson\n"
# "\n"
# "	Licensed under the Apache License, Version 2.0 (the \"License\");\n"
# "	you may not use this file except in compliance with the License.\n"
# "	You may obtain a copy of the License at\n"
# "\n"
# "		http://www.apache.org/licenses/LICENSE-2.0\n"
# "\n"
# "	Unless required by applicable law or agreed to in writing, software\n"
# "	distributed under the License is distributed on an \"AS IS\" BASIS,\n"
# "	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n"
# "	See the License for the specific language governing permissions and\n"
# "	limitations under the License.\n"
# "*/\n"
# "\n"
# "/*\n"
# "	COLOR_DARK     = #191919\n"
# "	COLOR_MEDIUM   = #353535\n"
# "	COLOR_MEDLIGHT = #5A5A5A\n"
# "	COLOR_LIGHT    = #DDDDDD\n"
# "	COLOR_ACCENT   = #3D7848\n"
# "*/\n"
# "\n"
# "* {\n"
# "	background: #191919;\n"
# "	color: #DDDDDD;\n"
# "	border: 1px solid #5A5A5A;\n"
# "}\n"
# "\n"
# "QWidget::item:selected {\n"
# "	background: #3D7848;\n"
# "}\n"
# "\n"
# "QCheckBox, QRadioButton {\n"
# "	border: none;\n"
# "}\n"
# ""
#                         "\n"
# "QRadioButton::indicator, QCheckBox::indicator {\n"
# "	width: 13px;\n"
# "	height: 13px;\n"
# "}\n"
# "\n"
# "QRadioButton::indicator::unchecked, QCheckBox::indicator::unchecked {\n"
# "	border: 1px solid #5A5A5A;\n"
# "	background: none;\n"
# "}\n"
# "\n"
# "QRadioButton::indicator:unchecked:hover, QCheckBox::indicator:unchecked:hover {\n"
# "	border: 1px solid #DDDDDD;\n"
# "}\n"
# "\n"
# "QRadioButton::indicator::checked, QCheckBox::indicator::checked {\n"
# "	border: 1px solid #5A5A5A;\n"
# "	background: #5A5A5A;\n"
# "}\n"
# "\n"
# "QRadioButton::indicator:checked:hover, QCheckBox::indicator:checked:hover {\n"
# "	border: 1px solid #DDDDDD;\n"
# "	background: #DDDDDD;\n"
# "}\n"
# "\n"
# "QGroupBox {\n"
# "	margin-top: 6px;\n"
# "}\n"
# "\n"
# "QGroupBox::title {\n"
# "	top: -7px;\n"
# "	left: 7px;\n"
# "}\n"
# "\n"
# "QScrollBar {\n"
# "	border: 1px solid #5A5A5A;\n"
# "	background: #191919;\n"
# "}\n"
# "\n"
# "QScrollBar:horizontal {\n"
# "	height: 15px;\n"
# "	margin: 0px 0px 0px 32px;\n"
# "}\n"
# "\n"
# "QScrollBar:vertical {\n"
# "	width: 15px;\n"
# "	margin: 32px 0px 0px 0px;\n"
# ""
#                         "}\n"
# "\n"
# "QScrollBar::handle {\n"
# "	background: #353535;\n"
# "	border: 1px solid #5A5A5A;\n"
# "}\n"
# "\n"
# "QScrollBar::handle:horizontal {\n"
# "	border-width: 0px 1px 0px 1px;\n"
# "}\n"
# "\n"
# "QScrollBar::handle:vertical {\n"
# "	border-width: 1px 0px 1px 0px;\n"
# "}\n"
# "\n"
# "QScrollBar::handle:horizontal {\n"
# "	min-width: 20px;\n"
# "}\n"
# "\n"
# "QScrollBar::handle:vertical {\n"
# "	min-height: 20px;\n"
# "}\n"
# "\n"
# "QScrollBar::add-line, QScrollBar::sub-line {\n"
# "	background:#353535;\n"
# "	border: 1px solid #5A5A5A;\n"
# "	subcontrol-origin: margin;\n"
# "}\n"
# "\n"
# "QScrollBar::add-line {\n"
# "	position: absolute;\n"
# "}\n"
# "\n"
# "QScrollBar::add-line:horizontal {\n"
# "	width: 15px;\n"
# "	subcontrol-position: left;\n"
# "	left: 15px;\n"
# "}\n"
# "\n"
# "QScrollBar::add-line:vertical {\n"
# "	height: 15px;\n"
# "	subcontrol-position: top;\n"
# "	top: 15px;\n"
# "}\n"
# "\n"
# "QScrollBar::sub-line:horizontal {\n"
# "	width: 15px;\n"
# "	subcontrol-position: top left;\n"
# "}\n"
# "\n"
# "QScrollBar::sub-line:vertical {\n"
# "	height: 15px;\n"
# "	subcontrol-position"
#                         ": top;\n"
# "}\n"
# "\n"
# "QScrollBar:left-arrow, QScrollBar::right-arrow, QScrollBar::up-arrow, QScrollBar::down-arrow {\n"
# "	border: 1px solid #5A5A5A;\n"
# "	width: 3px;\n"
# "	height: 3px;\n"
# "}\n"
# "\n"
# "QScrollBar::add-page, QScrollBar::sub-page {\n"
# "	background: none;\n"
# "}\n"
# "\n"
# "QAbstractButton:hover {\n"
# "	background: #353535;\n"
# "}\n"
# "\n"
# "QAbstractButton:pressed {\n"
# "	background: #5A5A5A;\n"
# "}\n"
# "\n"
# "QAbstractItemView {\n"
# "	show-decoration-selected: 1;\n"
# "	selection-background-color: #3D7848;\n"
# "	selection-color: #DDDDDD;\n"
# "	alternate-background-color: #353535;\n"
# "}\n"
# "\n"
# "QHeaderView {\n"
# "	border: 1px solid #5A5A5A;\n"
# "}\n"
# "\n"
# "QHeaderView::section {\n"
# "	background: #191919;\n"
# "	border: 1px solid #5A5A5A;\n"
# "	padding: 4px;\n"
# "}\n"
# "\n"
# "QHeaderView::section:selected, QHeaderView::section::checked {\n"
# "	background: #353535;\n"
# "}\n"
# "\n"
# "QTableView {\n"
# "	gridline-color: #5A5A5A;\n"
# "}\n"
# "\n"
# "QTabBar {\n"
# "	margin-left: 2px;\n"
# "}\n"
# "\n"
# "QTabBar::tab {\n"
# "	border-radius: 0px;\n"
# ""
#                         "	padding: 4px;\n"
# "	margin: 4px;\n"
# "}\n"
# "\n"
# "QTabBar::tab:selected {\n"
# "	background: #353535;\n"
# "}\n"
# "\n"
# "QComboBox::down-arrow {\n"
# "	border: 1px solid #5A5A5A;\n"
# "	background: #353535;\n"
# "}\n"
# "\n"
# "QComboBox::drop-down {\n"
# "	border: 1px solid #5A5A5A;\n"
# "	background: #353535;\n"
# "}\n"
# "\n"
# "QComboBox::down-arrow {\n"
# "	width: 3px;\n"
# "	height: 3px;\n"
# "	border: 1px solid #5A5A5A;\n"
# "}\n"
# "\n"
# "QAbstractSpinBox {\n"
# "	padding-right: 15px;\n"
# "}\n"
# "\n"
# "QAbstractSpinBox::up-button, QAbstractSpinBox::down-button {\n"
# "	border: 1px solid #5A5A5A;\n"
# "	background: #353535;\n"
# "	subcontrol-origin: border;\n"
# "}\n"
# "\n"
# "QAbstractSpinBox::up-arrow, QAbstractSpinBox::down-arrow {\n"
# "	width: 3px;\n"
# "	height: 3px;\n"
# "	border: 1px solid #5A5A5A;\n"
# "}\n"
# "\n"
# "QSlider {\n"
# "	border: none;\n"
# "}\n"
# "\n"
# "QSlider::groove:horizontal {\n"
# "	height: 5px;\n"
# "	margin: 4px 0px 4px 0px;\n"
# "}\n"
# "\n"
# "QSlider::groove:vertical {\n"
# "	width: 5px;\n"
# "	margin: 0px 4px 0px 4px;\n"
# "}\n"
# "\n"
# "QSlider::handle {\n"
# ""
#                         "	border: 1px solid #5A5A5A;\n"
# "	background: #353535;\n"
# "}\n"
# "\n"
# "QSlider::handle:horizontal {\n"
# "	width: 15px;\n"
# "	margin: -4px 0px -4px 0px;\n"
# "}\n"
# "\n"
# "QSlider::handle:vertical {\n"
# "	height: 15px;\n"
# "	margin: 0px -4px 0px -4px;\n"
# "}\n"
# "\n"
# "QSlider::add-page:vertical, QSlider::sub-page:horizontal {\n"
# "	background: #3D7848;\n"
# "}\n"
# "\n"
# "QSlider::sub-page:vertical, QSlider::add-page:horizontal {\n"
# "	background: #353535;\n"
# "}\n"
# "\n"
# "QLabel {\n"
# "	border: none;\n"
# "}\n"
# "\n"
# "QProgressBar {\n"
# "	text-align: center;\n"
# "}\n"
# "\n"
# "QProgressBar::chunk {\n"
# "	width: 1px;\n"
# "	background-color: #3D7848;\n"
# "}\n"
# "\n"
# "QMenu::separator {\n"
# "	background: #353535;\n"
# "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 261, 471))
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 30, 91, 22))
        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(10, 60, 91, 22))
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(300, 110, 431, 161))
        self.plainTextEdit_2 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(300, 290, 431, 161))
        self.plainTextEdit_2.setReadOnly(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(300, 460, 80, 24))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(410, 460, 121, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Split", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Combine", None))
        self.plainTextEdit.setDocumentTitle("")
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ASDasdas", None))
        self.plainTextEdit_2.setDocumentTitle("")
        self.plainTextEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save result to file", None))
    # retranslateUi

