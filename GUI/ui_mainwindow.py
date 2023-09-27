# -*- coding: utf-8 -*-
import qdarkstyle

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QMainWindow, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QWidget, QSpinBox, QLabel)

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 519)
        MainWindow.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='PySide6'))
        custom_font = QFont()
        custom_font.setPointSize(11)
        QApplication.setFont(custom_font, "QLabel")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 261, 471))
        self.radioButton_split = QRadioButton(self.groupBox)
        self.radioButton_split.setObjectName(u"radioButton")
        self.radioButton_split.setGeometry(QRect(10, 30, 91, 22))
        self.radioButton_split.setChecked(True)
        self.radioButton_combine = QRadioButton(self.groupBox)
        self.radioButton_combine.setObjectName(u"radioButton_2")
        self.radioButton_combine.setGeometry(QRect(70, 30, 91, 22))
        self.label_n = QLabel(self.groupBox)
        self.label_n.setGeometry(10, 60, 91, 25)
        self.spinBox_n = QSpinBox(self.groupBox)
        self.spinBox_n.setObjectName(u"spinBox_n")
        self.spinBox_n.setGeometry(QRect(40, 60, 91, 25))
        self.spinBox_n.setMaximum(10)
        self.spinBox_n.setValue(4)
        self.label_k = QLabel(self.groupBox)
        self.label_k.setGeometry(10, 90, 91, 25)
        self.spinBox_k = QSpinBox(self.groupBox)
        self.spinBox_k.setObjectName(u"spinBox_k")
        self.spinBox_k.setGeometry(QRect(40, 90, 91, 25))
        self.spinBox_k.setMaximum(10)
        self.spinBox_k.setValue(3)
        self.groupBox_seed = QGroupBox(self.groupBox)
        self.groupBox_seed.setObjectName(u"groupBox_seed")
        self.groupBox_seed.setGeometry(QRect(10, 120, 151, 100))
        self.radioButton_clock = QRadioButton(self.groupBox_seed)
        self.radioButton_clock.setObjectName(u"radioButton_clock")
        self.radioButton_clock.setGeometry(QRect(10, 10, 82, 22))
        self.radioButton_clock.setChecked(True)
        self.spinBox_custom_seed = QSpinBox(self.groupBox_seed)
        self.spinBox_custom_seed.setObjectName(u"spinBox_custom_seed")
        self.spinBox_custom_seed.setEnabled(False)
        self.spinBox_custom_seed.setGeometry(QRect(10, 60, 89, 25))
        self.spinBox_custom_seed.setMaximum(10000000)
        self.radioButton_custom = QRadioButton(self.groupBox_seed)
        self.radioButton_custom.setObjectName(u"radioButton_custom")
        self.radioButton_custom.setGeometry(QRect(10, 30, 94, 22))

        self.plainTextEdit_input = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_input.setObjectName(u"plainTextEdit")
        self.plainTextEdit_input.setGeometry(QRect(300, 110, 431, 161))
        self.plainTextEdit_result = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_result.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_result.setGeometry(QRect(300, 290, 431, 161))
        self.plainTextEdit_result.setReadOnly(True)
        self.pushButton_convert = QPushButton(self.centralwidget)
        self.pushButton_convert.setObjectName(u"pushButton")
        self.pushButton_convert.setGeometry(QRect(300, 460, 80, 24))
        # self.pushButton_save_to_file = QPushButton(self.centralwidget)
        # self.pushButton_save_to_file.setObjectName(u"pushButton_2")
        # self.pushButton_save_to_file.setGeometry(QRect(410, 460, 121, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        # set signals
        self.pushButton_convert.clicked.connect(MainWindow.convert)
        self.spinBox_k.valueChanged.connect(MainWindow.spinBox_k_validate)
        self.spinBox_n.valueChanged.connect(MainWindow.spinBox_n_validate)
        self.radioButton_custom.toggled.connect(self.spinBox_custom_seed.setEnabled)

        self.radioButton_split.toggled.connect(MainWindow.split_toggle_handler)
        self.radioButton_combine.toggled.connect(MainWindow.combine_toggle_handler)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.radioButton_split.setText(QCoreApplication.translate("MainWindow", u"Split", None))
        self.radioButton_combine.setText(QCoreApplication.translate("MainWindow", u"Combine", None))
        self.plainTextEdit_input.setDocumentTitle("")
        self.plainTextEdit_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.plainTextEdit_result.setDocumentTitle("")
        self.plainTextEdit_result.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.pushButton_convert.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        # self.pushButton_save_to_file.setText(QCoreApplication.translate("MainWindow", u"Save result to file", None))
        self.label_n.setText(QCoreApplication.translate("MainWindow", u"n =", None))
        self.label_k.setText(QCoreApplication.translate("MainWindow", u"k =", None))
        self.radioButton_clock.setText(QCoreApplication.translate("MainWindow", u"clock seed", None))
        self.radioButton_custom.setText(QCoreApplication.translate("MainWindow", u"custom seed", None))
    # retranslateUi

