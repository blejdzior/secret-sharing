from PySide6.QtWidgets import QApplication, QMainWindow
from GUI.ui_mainwindow import Ui_MainWindow
from algorithm.automata import Automata
import time
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
        f = open("result.txt", "w")
        f1 = open("result_combine.txt", "w")
        try:
            for i in range(20):
                self.k = 6
                self.n = 7
                r = 200
                start = time.time()
                self.automata = Automata(self.is_split, self.input, self.n, self.k, self.seed, r)
                end = time.time()
                print(end - start)
                f.write("{}\n".format(end - start))
                start = time.time()

                string = "k = {0:<5}\nn = {1:<5}\nr = {2:<5}\nrules = {3:10}\n{4}".format(self.automata.k,
                                                                                          self.automata.n,
                                                                                          self.automata.r,
                                                                                          ', '.join(str(i) for i in
                                                                                                    self.automata.rules_int),
                                                                                          "\n".join(
                                                                                              ": ".join(str(j) for j in
                                                                                                        self.automata.automata[
                                                                                                            i]) for i in
                                                                                              range(
                                                                                                  len(self.automata.automata) - 1,
                                                                                                  len(self.automata.automata) - self.n - 1,
                                                                                                  -1))
                                                                                          )
                end = time.time()
                print(end - start)


                start = time.time()
                self.automata = Automata(False, string, self.n, self.k, self.seed, r)
                end = time.time()
                print(end - start)
                f1.write("{}\n".format(end - start))

            f.write("\n")
            f1.write("\n")
            for i in range(20):
                self.k = 3
                self.n = 5
                r = 200
                start = time.time()
                self.automata = Automata(self.is_split, self.input, self.n, self.k, self.seed, r)
                end = time.time()
                print(end - start)
                f.write("{}\n".format(end - start))

                string = "k = {0:<5}\nn = {1:<5}\nr = {2:<5}\nrules = {3:10}\n{4}".format(self.automata.k,
                                                                                          self.automata.n,
                                                                                          self.automata.r,
                                                                                          ', '.join(str(i) for i in
                                                                                                    self.automata.rules_int),
                                                                                          "\n".join(
                                                                                              ": ".join(str(j) for j in
                                                                                                        self.automata.automata[
                                                                                                            i]) for i in
                                                                                              range(
                                                                                                  len(self.automata.automata) - 1,
                                                                                                  len(self.automata.automata) - self.n - 1,
                                                                                                  -1))
                                                                                          )

                start = time.time()
                self.automata = Automata(False, string, self.n, self.k, self.seed, r)
                end = time.time()
                print(end - start)
                f1.write("{}\n".format(end - start))

            f.write("\n")
            f1.write("\n")
            for i in range(20):
                self.k = 2
                self.n = 3
                r = 200
                start = time.time()
                self.automata = Automata(self.is_split, self.input, self.n, self.k, self.seed, r)
                end = time.time()
                print(end - start)
                f.write("{}\n".format(end - start))

                string = "k = {0:<5}\nn = {1:<5}\nr = {2:<5}\nrules = {3:10}\n{4}".format(self.automata.k,
                                                                                          self.automata.n,
                                                                                          self.automata.r,
                                                                                          ', '.join(str(i) for i in
                                                                                                    self.automata.rules_int),
                                                                                          "\n".join(
                                                                                              ": ".join(str(j) for j in
                                                                                                        self.automata.automata[
                                                                                                            i]) for i in
                                                                                              range(
                                                                                                  len(self.automata.automata) - 1,
                                                                                                  len(self.automata.automata) - self.n - 1,
                                                                                                  -1))
                                                                                          )

                start = time.time()
                self.automata = Automata(False, string, self.n, self.k, self.seed, r)
                end = time.time()
                print(end - start)
                f1.write("{}\n".format(end - start))

            f.write("\n")
            f1.write("\n")
            for i in range(20):
                self.k = 6
                self.n = 7
                r = 100
                start = time.time()
                self.automata = Automata(self.is_split, self.input, self.n, self.k, self.seed, r)
                end = time.time()
                print(end - start)
                f.write("{}\n".format(end - start))

                string = "k = {0:<5}\nn = {1:<5}\nr = {2:<5}\nrules = {3:10}\n{4}".format(self.automata.k,
                                                                                          self.automata.n,
                                                                                          self.automata.r,
                                                                                          ', '.join(str(i) for i in
                                                                                                    self.automata.rules_int),
                                                                                          "\n".join(
                                                                                              ": ".join(str(j) for j in
                                                                                                        self.automata.automata[
                                                                                                            i]) for i in
                                                                                              range(
                                                                                                  len(self.automata.automata) - 1,
                                                                                                  len(self.automata.automata) - self.n - 1,
                                                                                                  -1))
                                                                                          )

                start = time.time()
                self.automata = Automata(False, string, self.n, self.k, self.seed, r)
                end = time.time()
                print(end - start)
                f1.write("{}\n".format(end - start))

            f.write("\n")
            f1.write("\n")
            for i in range(20):
                self.k = 3
                self.n = 5
                r = 100
                start = time.time()
                self.automata = Automata(self.is_split, self.input, self.n, self.k, self.seed, r)
                end = time.time()
                print(end - start)
                f.write("{}\n".format(end - start))

                string = "k = {0:<5}\nn = {1:<5}\nr = {2:<5}\nrules = {3:10}\n{4}".format(self.automata.k,
                                                                                          self.automata.n,
                                                                                          self.automata.r,
                                                                                          ', '.join(str(i) for i in
                                                                                                    self.automata.rules_int),
                                                                                          "\n".join(
                                                                                              ": ".join(str(j) for j in
                                                                                                        self.automata.automata[
                                                                                                            i]) for i in
                                                                                              range(
                                                                                                  len(self.automata.automata) - 1,
                                                                                                  len(self.automata.automata) - self.n - 1,
                                                                                                  -1))
                                                                                          )

                start = time.time()
                self.automata = Automata(False, string, self.n, self.k, self.seed, r)
                end = time.time()
                print(end - start)
                f1.write("{}\n".format(end - start))

            f.write("\n")
            f1.write("\n")
            for i in range(20):
                self.k = 2
                self.n = 3
                r = 100
                start = time.time()
                self.automata = Automata(self.is_split, self.input, self.n, self.k, self.seed, r)
                end = time.time()
                print(end - start)
                f.write("{}\n".format(end - start))

                string = "k = {0:<5}\nn = {1:<5}\nr = {2:<5}\nrules = {3:10}\n{4}".format(self.automata.k,
                                                                                          self.automata.n,
                                                                                          self.automata.r,
                                                                                          ', '.join(str(i) for i in
                                                                                                    self.automata.rules_int),
                                                                                          "\n".join(
                                                                                              ": ".join(str(j) for j in
                                                                                                        self.automata.automata[
                                                                                                            i]) for i in
                                                                                              range(
                                                                                                  len(self.automata.automata) - 1,
                                                                                                  len(self.automata.automata) - self.n - 1,
                                                                                                  -1))
                                                                                          )

                start = time.time()
                self.automata = Automata(False, string, self.n, self.k, self.seed, r)
                end = time.time()
                print(end - start)
                f1.write("{}\n".format(end - start))

            f.write("\n")
            f1.write("\n")
            for i in range(20):
                self.k = 6
                self.n = 7
                r = 10
                start = time.time()
                self.automata = Automata(self.is_split, self.input, self.n, self.k, self.seed, r)
                end = time.time()
                print(end - start)
                f.write("{}\n".format(end - start))

                string = "k = {0:<5}\nn = {1:<5}\nr = {2:<5}\nrules = {3:10}\n{4}".format(self.automata.k,
                                                                                          self.automata.n,
                                                                                          self.automata.r,
                                                                                          ', '.join(str(i) for i in
                                                                                                    self.automata.rules_int),
                                                                                          "\n".join(
                                                                                              ": ".join(str(j) for j in
                                                                                                        self.automata.automata[
                                                                                                            i]) for i in
                                                                                              range(
                                                                                                  len(self.automata.automata) - 1,
                                                                                                  len(self.automata.automata) - self.n - 1,
                                                                                                  -1))
                                                                                          )

                start = time.time()
                self.automata = Automata(False, string, self.n, self.k, self.seed, r)
                end = time.time()
                print(end - start)
                f1.write("{}\n".format(end - start))

            f.write("\n")
            f1.write("\n")
            for i in range(20):
                self.k = 3
                self.n = 5
                r = 10
                start = time.time()
                self.automata = Automata(self.is_split, self.input, self.n, self.k, self.seed, r)
                end = time.time()
                print(end - start)
                f.write("{}\n".format(end - start))

                string = "k = {0:<5}\nn = {1:<5}\nr = {2:<5}\nrules = {3:10}\n{4}".format(self.automata.k,
                                                                                          self.automata.n,
                                                                                          self.automata.r,
                                                                                          ', '.join(str(i) for i in
                                                                                                    self.automata.rules_int),
                                                                                          "\n".join(
                                                                                              ": ".join(str(j) for j in
                                                                                                        self.automata.automata[
                                                                                                            i]) for i in
                                                                                              range(
                                                                                                  len(self.automata.automata) - 1,
                                                                                                  len(self.automata.automata) - self.n - 1,
                                                                                                  -1))
                                                                                          )

                start = time.time()
                self.automata = Automata(False, string, self.n, self.k, self.seed, r)
                end = time.time()
                print(end - start)
                f1.write("{}\n".format(end - start))

            f.write("\n")
            f1.write("\n")
            for i in range(20):
                self.k = 2
                self.n = 3
                r = 10
                start = time.time()
                self.automata = Automata(self.is_split, self.input, self.n, self.k, self.seed, r)
                end = time.time()
                print(end - start)
                f.write("{}\n".format(end - start))

                string = "k = {0:<5}\nn = {1:<5}\nr = {2:<5}\nrules = {3:10}\n{4}".format(self.automata.k,
                                                                                          self.automata.n,
                                                                                          self.automata.r,
                                                                                          ', '.join(str(i) for i in
                                                                                                    self.automata.rules_int),
                                                                                          "\n".join(
                                                                                              ": ".join(str(j) for j in
                                                                                                        self.automata.automata[
                                                                                                            i]) for i in
                                                                                              range(
                                                                                                  len(self.automata.automata) - 1,
                                                                                                  len(self.automata.automata) - self.n - 1,
                                                                                                  -1))
                                                                                          )

                start = time.time()
                self.automata = Automata(False, string, self.n, self.k, self.seed, r)
                end = time.time()
                print(end - start)
                f1.write("{}\n".format(end - start))

            f.write("\n")
            f1.write("\n")


        except UnicodeDecodeError as err:
            self.ui.plainTextEdit_result.clear()
            self.ui.plainTextEdit_result.insertPlainText("Unicode Error.\nPossibly not enough automata states provided.")
            raise err
        except ValueError as err:
            self.ui.plainTextEdit_result.clear()
            self.ui.plainTextEdit_result.insertPlainText("Missing data.\nProvide values of m, n, k, r, rules, and k states of automata")
            raise err
        except IndexError as err:
            self.ui.plainTextEdit_result.clear()
            self.ui.plainTextEdit_result.insertPlainText("Index error.\npossibly not enough automata states provided.")
            raise err

        if self.is_split:
            self.save_result_split()
        else:
            self.save_result_combine()

    # saves input from GUI
    def set_data(self):
        self.input = self.ui.plainTextEdit_input.toPlainText()
        self.is_split = self.ui.radioButton_split.isChecked()
        self.k = self.ui.spinBox_k.value()
        self.n = self.ui.spinBox_n.value()
        if self.ui.radioButton_custom.isChecked():
            self.seed = self.ui.spinBox_custom_seed.value()
        else:
            self.seed = None

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

    def save_result_split(self):
        self.ui.plainTextEdit_result.clear()
        string = "k = {0:<5}\nn = {1:<5}\nr = {2:<5}\nrules = {3:10}\n".format(self.automata.k,
                                                                                           self.automata.n,
                                                                                           self.automata.r,
                                                                                            ', '.join(str(i) for i in self.automata.rules_int),
                                                                                           )
        self.ui.plainTextEdit_result.insertPlainText(string)
        string = "\n".join(": ".join(str(j) for j in self.automata.automata[i]) for i in range(len(self.automata.automata) - 1,
                                                                               len(self.automata.automata) - self.n - 1,
                                                                               -1))
        self.ui.plainTextEdit_result.insertPlainText(string)

    def save_result_combine(self):
        self.ui.plainTextEdit_result.clear()
        self.ui.plainTextEdit_result.insertPlainText(self.automata.result)



    def split_toggle_handler(self):
        self.ui.spinBox_k.setEnabled(True)
        self.ui.spinBox_n.setEnabled(True)
        self.ui.groupBox_seed.setEnabled(True)


    def combine_toggle_handler(self):
        self.ui.spinBox_k.setEnabled(False)
        self.ui.spinBox_n.setEnabled(False)
        self.ui.groupBox_seed.setEnabled(False)