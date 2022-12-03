import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QObject
from threading import Thread
from chess import Ui_MainWindow


class Communication(QObject):
    dataSignal = pyqtSignal(int, int)


class Chess(QMainWindow):
    def __init__(self):
        super(Chess, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.comm = Communication()
        self.comm.dataSignal.connect(self.go)
        print('ok')

    @pyqtSlot(int, int)
    def go(self, i, j):
        print('ok1')
        r, g, b = np.random.uniform(0, 255, 3)
        btn = self.ui._3[i * 10 + j]
        btn.setStyleSheet(f"background-color : rgb({r}, {g}, {b})")
        print('ok2')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Chess()
    sys.exit(app.exec_())