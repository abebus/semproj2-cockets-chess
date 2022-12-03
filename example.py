import sys
import numpy as np
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QGridLayout
from calc import Ui_MainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QObject
from threading import Thread
from time import sleep
import sys


class Communication(QObject):
    dataSignal = pyqtSignal(str)


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # это для показа
        self.dcl_ = ''
        # это для работы
        self.str_ = ''
        self.ui.button_1.clicked.connect(self.number_clicked)
        self.ui.button_2.clicked.connect(self.number_clicked)
        self.ui.button_3.clicked.connect(self.number_clicked)
        self.ui.button_4.clicked.connect(self.number_clicked)
        self.ui.button_5.clicked.connect(self.number_clicked)
        self.ui.button_6.clicked.connect(self.number_clicked)
        self.ui.button_7.clicked.connect(self.number_clicked)
        self.ui.button_8.clicked.connect(self.number_clicked)
        self.ui.button_9.clicked.connect(self.number_clicked)
        self.ui.button_0.clicked.connect(self.number_clicked)
        self.ui.plus.clicked.connect(self.operation_clicked)
        self.ui.minus.clicked.connect(self.operation_clicked)
        self.ui.mult.clicked.connect(self.operation_clicked)
        self.ui.div.clicked.connect(self.operation_clicked)
        self.ui.clear.clicked.connect(self.clear)
        self.ui.equal.clicked.connect(self.calculate)

    def number_clicked(self):
        if self.str_[-1] != '/':
            sender = self.sender()
            self.ui.lcdNumber.display(self.dcl_ + sender.text())
            self.dcl_ += sender.text()
            self.str_ += sender.text()
        else:
            pass

    def operation_clicked(self):
        if self.str_ and self.str_[-1] not in set('+-/*'):
            self.str_ += self.sender().text()
            self.dcl_ = ''
            self.ui.lcdNumber.display(self.dcl_)
        else:
            pass

    def clear(self):
        self.str_ = ''
        self.dcl_ = ''
        self.ui.lcdNumber.display(self.dcl_)

    def calculate(self):
        if self.str_:
            self.ui.lcdNumber.display(eval(self.str_))
            self.dcl_ = ''
            self.str_ = ''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
