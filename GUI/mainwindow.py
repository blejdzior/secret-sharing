from PySide6.QtWidgets import QApplication, QMainWindow
from GUI.ui_mainwindow import Ui_MainWindow
from algorithm.automata import Automata

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.seed = None
        self.n = None
        self.k = None
        self.is_split = None
        self.input = None
        self.automata = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def convert(self):
        self.set_data()
        self.automata = Automata(self.is_split, self.input, self.n, self.k, self.seed)


    # saves input from GUI
    def set_data(self):
        self.input = self.ui.plainTextEdit_input.toPlainText()
        self.is_split = self.ui.radioButton_split.isChecked()
        self.k = self.ui.spinBox_k.value()
        self.n = self.ui.spinBox_n.value()
        if self.ui.radioButton_custom.isChecked():
            self.seed = self.ui.spinBox_custom_seed.value()


    # validates if k is smaller than n
    def spinBox_k_validate(self, value_k):
        value_n = self.ui.spinBox_n.value()
        if value_k >= value_n:
            self.ui.spinBox_k.setValue(value_n - 1)

    # verifies if after changing value of n, still k < n
    def spinBox_n_validate(self, value_n):
        value_k = self.ui.spinBox_k.value()
        if value_k >= value_n:
            self.ui.spinBox_k.setValue(value_n - 1)
