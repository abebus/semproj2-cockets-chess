import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QObject
from threading import Thread
from chess import Ui_MainWindow
from models import icons


class Communication(QObject):
    dataSignal = pyqtSignal(int, int)


class Chess(QMainWindow):
    def __init__(self):
        super(Chess, self).__init__()
        self.comm = Communication()
        self.comm.dataSignal.connect(self.variants)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.field = [[self.ui._11, self.ui._21, self.ui._31, self.ui._41, self.ui._51, self.ui._61, self.ui._71, self.ui._81],
                      [self.ui._12, self.ui._22, self.ui._32, self.ui._42, self.ui._52, self.ui._62, self.ui._72, self.ui._82],
                      [self.ui._13, self.ui._23, self.ui._33, self.ui._43, self.ui._53, self.ui._63, self.ui._73, self.ui._83],
                      [self.ui._14, self.ui._24, self.ui._34, self.ui._44, self.ui._54, self.ui._64, self.ui._74, self.ui._84],
                      [self.ui._15, self.ui._25, self.ui._35, self.ui._45, self.ui._55, self.ui._65, self.ui._75, self.ui._85],
                      [self.ui._16, self.ui._26, self.ui._36, self.ui._46, self.ui._56, self.ui._66, self.ui._76, self.ui._86],
                      [self.ui._17, self.ui._27, self.ui._37, self.ui._47, self.ui._57, self.ui._67, self.ui._77, self.ui._87],
                      [self.ui._18, self.ui._28, self.ui._38, self.ui._48, self.ui._58, self.ui._68, self.ui._78, self.ui._88]]
        self.construct_field()
        for lst in range(len(self.field)):
            for btn in range(len(self.field[lst])):
                self.field[lst][btn].clicked.connect(lambda state, x=btn, y=lst: self.variants(y, x))


    def construct_field(self):
        self.ui._11.setText(icons['wl'])
        self.ui._21.setText(icons['whorse'])
        self.ui._31.setText(icons['weleph'])
        self.ui._41.setText(icons['wking'])
        self.ui._51.setText(icons['wqueen'])
        self.ui._61.setText(icons['weleph'])
        self.ui._71.setText(icons['whorse'])
        self.ui._81.setText(icons['wl'])
        self.ui._18.setText(icons['bl'])
        self.ui._28.setText(icons['bhorse'])
        self.ui._38.setText(icons['beleph'])
        self.ui._48.setText(icons['bqueen'])
        self.ui._58.setText(icons['bking'])
        self.ui._68.setText(icons['beleph'])
        self.ui._78.setText(icons['bhorse'])
        self.ui._88.setText(icons['bl'])
        for i in self.field[1]:
            i.setText(icons['wp'])
        for i in self.field[6]:
            i.setText(icons['bp'])

    @pyqtSlot(int, int)
    def variants(self, y, x):
        txt = self.field[y][x].text()
        if txt == icons['wking']:
            vars_ = list(self.field[y + j][x + i] for j, i in
                     ((1, 1), (1, 0), (1, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1))
                     if 7 >= (y + j) >= 0 and 7 >= (x + i) >= 0)
            for btn in vars_:
                if btn.text() not in list(icons.values())[0:-1:2]:
                    btn.setStyleSheet('background-color:gray')
        elif txt == icons['bking']:
            vars_ = list(self.field[y + j][x + i] for j, i in
                         ((1, 1), (1, 0), (1, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1))
                         if 7 >= (y + j) >= 0 and 7 >= (x + i) >= 0)
            for btn in vars_:
                if btn.text() not in list(icons.values())[1:-1:2]:
                    btn.setStyleSheet('background-color:gray')
        elif txt == icons['whorse']:
            vars_ = list(self.field[y + j][x + i] for j, i in
                     ((2, 1), (-2, 1), (1, -2), (1, 2), (-2, -1), (2, -1), (-1, 2), (-1, -2))
                     if 7 >= (y + j) >= 0 and 7 >= (x + i) >= 0)
            for btn in vars_:
                if btn.text() not in list(icons.values())[0:-1:2]:
                    btn.setStyleSheet('background-color:gray')
        elif txt == icons['bhorse']:
            vars_ = list(self.field[y+j][x+i] for j, i in
                         ((2, 1), (-2, 1), (1, -2), (1, 2), (-2, -1), (2, -1), (-1, 2), (-1, -2))
                         if 7 >= (y+j) >= 0 and 7 >= (x+i) >= 0)
            for btn in vars_:
                if btn.text() not in list(icons.values())[1:-1:2]:
                    btn.setStyleSheet('background-color:gray')
        elif txt == icons['weleph']:
            vars_ = list(self.field[y+i][x+i] for i in range(-7, 8)
                         if 7 >= (x+i) >= 0 and 7 >= (y+i) >= 0 and y != (y+i) and x != (x+i)) + \
                    list(self.field[y - i][x + i] for i in range(-7, 8)
                         if 7 >= (x + i) >= 0 and 7 >= (y + i) >= 0 and y != (y + i) and x != (x + i))
            for btn in vars_:
                if btn.text() not in list(icons.values())[0:-1:2]:
                    btn.setStyleSheet('background-color:gray')
                    if btn.txt() in list(icons.values()[1:-1:2]):
                        break
                else:
                    break
        elif txt == icons['beleph']:
            vars_ = list(self.field[y+i][x+i] for i in range(-7, 8)
                         if 7 >= (x+i) >= 0 and 7 >= (y+i) >= 0 and y != (y+i) and x != (x+i)) + \
                    list(self.field[y - i][x + i] for i in range(-7, 8)
                         if 7 >= (x + i) >= 0 and 7 >= (y + i) >= 0 and y != (y + i) and x != (x + i))
            for btn in vars_:
                if btn.text() not in list(icons.values())[1:-1:2]:
                    btn.setStyleSheet('background-color:gray')
                    if btn.txt() in list(icons.values()[0:-1:2]):
                        break
                else:
                    break
        elif txt == icons['wl']:
            vars_ = list(self.field[y + i][x] for i in range(-7, 8)
                         if 7 >= (y + i) >= 0 and y != (y+i)) +\
                    list(self.field[y][x + i] for i in range(-7, 8)
                         if 7 >= (x + i) >= 0 and x != (x+i))
            for btn in vars_:
                if btn.text() not in list(icons.values())[0:-1:2]:
                    btn.setStyleSheet('background-color:gray')
                    if btn.txt() in list(icons.values()[1:-1:2]):
                        break
                else:
                    break
        elif txt == icons['bl']:
            vars_ = list(self.field[y + i][x] for i in range(-7, 8)
                         if 7 >= (y + i) >= 0 and y != (y+i)) +\
                    list(self.field[y][x + i] for i in range(-7, 8)
                         if 7 >= (x + i) >= 0 and x != (x+i))
            for btn in vars_:
                if btn.text() not in list(icons.values())[1:-1:2]:
                    btn.setStyleSheet('background-color:gray')
                    if btn.txt() in list(icons.values()[0:-1:2]):
                        break
                else:
                    break
        elif txt == icons['wqueen']:
            vars_ = list(self.field[y + i][x] for i in range(-7, 8)
                         if 7 >= (y + i) >= 0 and y != (y+i)) +\
                    list(self.field[y][x + i] for i in range(-7, 8)
                         if 7 >= (x + i) >= 0 and x != (x+i)) + \
                    list(self.field[y + i][x + i] for i in range(-7, 8)
                         if 7 >= (x + i) >= 0 and 7 >= (y + i) >= 0 and y != (y + i) and x != (x + i)) + \
                    list(self.field[y - i][x + i] for i in range(-7, 8)
                         if 7 >= (x + i) >= 0 and 7 >= (y + i) >= 0 and y != (y + i) and x != (x + i))
            for btn in vars_:
                if btn.text() not in list(icons.values())[0:-1:2]:
                    btn.setStyleSheet('background-color:gray')
                    if btn.txt() in list(icons.values()[1:-1:2]):
                        break
                else:
                    break
        elif txt == icons['bqueen']:
            vars_ = list(self.field[y + i][x] for i in range(-7, 8)
                         if 7 >= (y + i) >= 0 and y != (y+i)) +\
                    list(self.field[y][x + i] for i in range(-7, 8)
                         if 7 >= (x + i) >= 0 and x != (x+i)) + \
                    list(self.field[y + i][x + i] for i in range(-7, 8)
                         if 7 >= (x + i) >= 0 and 7 >= (y + i) >= 0 and y != (y + i) and x != (x + i)) + \
                    list(self.field[y - i][x + i] for i in range(-7, 8)
                         if 7 >= (x + i) >= 0 and 7 >= (y + i) >= 0 and y != (y + i) and x != (x + i))
            for btn in vars_:
                if btn.text() not in list(icons.values())[1:-1:2]:
                    btn.setStyleSheet('background-color:gray')
                    if btn.txt() in list(icons.values()[0:-1:2]):
                        break
                else:
                    break
        elif txt == icons['wp']:
            vars_ = list(self.field[y+j][x+i] for j, i in ((1, 0), (1, 1), (1, -1))
                         if 7 >= (x + i) >= 0 and 7 >= (y + i) >= 0)
            for btn in vars_:
                if (btn.text() not in list(icons.values())[0:-1:2] and btn == vars_[0])\
                or (btn.text() in list(icons.values())[1:-1:2] and btn != vars_[0]):
                    btn.setStyleSheet('background-color:gray')
        elif txt == icons['bp']:
            vars_ = list(self.field[y+j][x+i] for j, i in ((-1, 0), (-1, -1), (-1, 1))
                         if 7 >= (x + i) >= 0 and 7 >= (y + i) >= 0)
            for btn in vars_:
                if (btn.text() not in list(icons.values())[1:-1:2] and btn == vars_[0])\
                or (btn.text() in list(icons.values())[0:-1:2] and btn != vars_[0]):
                    btn.setStyleSheet('background-color:gray')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Chess()
    ex.show()
    sys.exit(app.exec_())