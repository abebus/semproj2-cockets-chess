import sys
import socket
import pickle
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject, QThread
from chess_gui import *
from models import icons
import helper as h


class BackendClient(QThread):
    address = ("127.0.0.1", 5432)

    def __init__(self, signal, name):
        super().__init__()
        self.name = name
        self.signal = signal

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(BackendClient.address)

    def run(self):
        while 1:
            binary_data = self.sock.recv(1024)
            if binary_data is None or not len(binary_data):
                break
            print(binary_data)
            info = pickle.loads(binary_data)
            #
            print(info)
            text = info.get('text')
            data = info.get('data')  # for example

            self.signal.emit(text)


class Communication(QObject):
    chess_Signal = pyqtSignal(int, int)
    msg_signal = pyqtSignal(str)


class Chess(Chess):
    # global startx
    # global starty
    def __init__(self):
        super().__init__()
        self.comm = Communication()
        self.comm.chess_Signal.connect(self.variants)
        self.comm.msg_signal.connect(self.recv_msg)
        #self.client = BackendClient(self.comm.msg_signal,name='a')
        #self.client.start()
        self.logic()
        for lst in range(len(self.field)):
            for btn in range(len(self.field[lst])):
                self.field[lst][btn].clicked.connect(lambda state, x=btn, y=lst: self.variants(y, x))



    def logic(self):
        self.findChild(QPushButton, 'btn_send_msg').clicked.connect(self.send_msg)
        # self.btn_clear.clicked.connect(self.clear_area)
        self.ui.chat_history.setText("Welcome fgdghggh")

    @pyqtSlot(str)
    def recv_msg(self, text):
        self.ui.chat_history.append(text)

    def send_msg(self):
        text: str = self.ui.lineEdit_2.text()
        if len(text.strip()) > 0:
            self.recv_msg(text)
            self.ui.lineEdit_2.setText("")
            # socket
            # self.client.send(text)

    @pyqtSlot(int, int)
    def variants(self, y, x):
        # print(y, x)
        # сначала чистим серые поля чтоб при нажатии на другую кнопку варианты хода менялись
        if self.field[y][x].text() != '':
            [self.field[i][j].setStyleSheet('background-color:#f2f2f2') for i in range(0, 8) for j in range(0, 8)
             if 7 >= i >= 0 and 7 >= j >= 0 and i % 2 == j % 2]
            [self.field[i][j].setStyleSheet('background-color: #404040') for i in range(0, 8) for j in range(0, 8)
             if 7 >= i >= 0 and 7 >= j >= 0 and i % 2 != j % 2]
        vars_ = []
        # тут просто берем иконку чтоб понять как ходить может !!!!!1 С ЕБУЧЕЙ КНОПКИ БЕРЁМ ТЕКСТ НЕЕЕЕТ НИЗЯ ТАК
        txt = self.field[y][x].text()
        if txt == icons['wking']:
            # тут закоменчу чист,далее не особо отличается
            # делаем список с вариантами хода и сразу проверяем,что он в пределах поля
            vars_ = list(self.field[y + j][x + i] for j, i in
                         ((1, 1), (1, 0), (1, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1))
                         if 7 >= (y + j) >= 0 and 7 >= (x + i) >= 0)
            # тут списком проходим и смотрим чтоб не сходил на своих ребят
            for btn in vars_:
                if btn.text() not in list(icons.values())[0::2]:
                    btn.setStyleSheet('background-color:gray')
        elif txt == icons['bking']:
            vars_ = list(self.field[y + j][x + i] for j, i in
                         ((1, 1), (1, 0), (1, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1))
                         if 7 >= (y + j) >= 0 and 7 >= (x + i) >= 0)
            for btn in vars_:
                if btn.text() not in list(icons.values())[1::2]:
                    btn.setStyleSheet('background-color:gray')
        elif txt == icons['whorse']:
            vars_ = list(self.field[y + j][x + i] for j, i in
                         ((2, 1), (-2, 1), (1, -2), (1, 2), (-2, -1), (2, -1), (-1, 2), (-1, -2))
                         if 7 >= (y + j) >= 0 and 7 >= (x + i) >= 0)
            for btn in vars_:
                if btn.text() not in list(icons.values())[0::2]:
                    btn.setStyleSheet('background-color:gray')
        elif txt == icons['bhorse']:
            vars_ = list(self.field[y + j][x + i] for j, i in
                         ((2, 1), (-2, 1), (1, -2), (1, 2), (-2, -1), (2, -1), (-1, 2), (-1, -2))
                         if 7 >= (y + j) >= 0 and 7 >= (x + i) >= 0)
            for btn in vars_:
                if btn.text() not in list(icons.values())[1::2]:
                    btn.setStyleSheet('background-color:gray')
        elif txt == icons['weleph']:
            vars_ = [list(self.field[y + i][x + i] for i in range(1, 8)
                          if 7 >= (x + i) >= 0 and 7 >= (y + i) >= 0),
                     list(self.field[y - i][x + i] for i in range(1, 8)
                          if 7 >= (x + i) >= 0 and 7 >= (y - i) >= 0),
                     list(self.field[y + i][x - i] for i in range(1, 8)
                          if 7 >= (x - i) >= 0 and 7 >= (y + i) >= 0),
                     list(self.field[y - i][x - i] for i in range(1, 8)
                          if 7 >= (x - i) >= 0 and 7 >= (y - i) >= 0)]
            for lst in vars_:
                for btn in lst:
                    if btn.text() not in list(icons.values())[0::2]:
                        btn.setStyleSheet('background-color:gray')
                        if btn.text() in list(icons.values())[1::2]:
                            break
                        continue
                    break
        elif txt == icons['beleph']:
            vars_ = [list(self.field[y + i][x + i] for i in range(1, 8)
                          if 7 >= (x + i) >= 0 and 7 >= (y + i) >= 0),
                     list(self.field[y - i][x + i] for i in range(1, 8)
                          if 7 >= (x + i) >= 0 and 7 >= (y - i) >= 0),
                     list(self.field[y + i][x - i] for i in range(1, 8)
                          if 7 >= (x - i) >= 0 and 7 >= (y + i) >= 0),
                     list(self.field[y - i][x - i] for i in range(1, 8)
                          if 7 >= (x - i) >= 0 and 7 >= (y - i) >= 0)]
            for lst in vars_:
                for btn in lst:
                    if btn.text() not in list(icons.values())[1::2]:
                        btn.setStyleSheet('background-color:gray')
                        if btn.text() in list(icons.values())[0::2]:
                            break
                        continue
                    break
        elif txt == icons['wl']:
            vars_ = [list(self.field[y][x + i] for i in range(1, 8)
                          if 7 >= (x + i) >= 0),
                     list(self.field[y + i][x] for i in range(1, 8)
                          if 7 >= (y + i) >= 0),
                     list(self.field[y][x - i] for i in range(1, 8)
                          if 7 >= (x - i) >= 0),
                     list(self.field[y - i][x] for i in range(1, 8)
                          if 7 >= (y - i) >= 0)]
            for lst in vars_:
                for btn in lst:
                    if btn.text() not in list(icons.values())[0::2]:
                        btn.setStyleSheet('background-color:gray')
                        if btn.text() in list(icons.values())[1::2]:
                            break
                        continue
                    break
        elif txt == icons['bl']:
            vars_ = [list(self.field[y][x + i] for i in range(1, 8)
                          if 7 >= (x + i) >= 0),
                     list(self.field[y + i][x] for i in range(1, 8)
                          if 7 >= (y + i) >= 0),
                     list(self.field[y][x - i] for i in range(1, 8)
                          if 7 >= (x - i) >= 0),
                     list(self.field[y - i][x] for i in range(1, 8)
                          if 7 >= (y - i) >= 0)]
            for lst in vars_:
                for btn in lst:
                    if btn.text() not in list(icons.values())[1::2]:
                        btn.setStyleSheet('background-color:gray')
                        if btn.text() in list(icons.values())[0::2]:
                            break
                        continue
                    break
        elif txt == icons['wqueen']:
            vars_ = [list(self.field[y][x + i] for i in range(1, 8)
                          if 7 >= (x + i) >= 0),
                     list(self.field[y + i][x] for i in range(1, 8)
                          if 7 >= (y + i) >= 0),
                     list(self.field[y][x - i] for i in range(1, 8)
                          if 7 >= (x - i) >= 0),
                     list(self.field[y - i][x] for i in range(1, 8)
                          if 7 >= (y - i) >= 0),
                     list(self.field[y + i][x + i] for i in range(1, 8)
                          if 7 >= (x + i) >= 0 and 7 >= (y + i) >= 0),
                     list(self.field[y - i][x + i] for i in range(1, 8)
                          if 7 >= (x + i) >= 0 and 7 >= (y - i) >= 0),
                     list(self.field[y + i][x - i] for i in range(1, 8)
                          if 7 >= (x - i) >= 0 and 7 >= (y + i) >= 0),
                     list(self.field[y - i][x - i] for i in range(1, 8)
                          if 7 >= (x - i) >= 0 and 7 >= (y - i) >= 0)]
            for lst in vars_:
                for btn in lst:
                    if btn.text() not in list(icons.values())[0::2]:
                        btn.setStyleSheet('background-color:gray')
                        if btn.text() in list(icons.values())[1::2]:
                            break
                        continue
                    break
        elif txt == icons['bqueen']:
            vars_ = [list(self.field[y][x + i] for i in range(1, 8)
                          if 7 >= (x + i) >= 0),
                     list(self.field[y + i][x] for i in range(1, 8)
                          if 7 >= (y + i) >= 0),
                     list(self.field[y][x - i] for i in range(1, 8)
                          if 7 >= (x - i) >= 0),
                     list(self.field[y - i][x] for i in range(1, 8)
                          if 7 >= (y - i) >= 0),
                     list(self.field[y + i][x + i] for i in range(1, 8)
                          if 7 >= (x + i) >= 0 and 7 >= (y + i) >= 0),
                     list(self.field[y - i][x + i] for i in range(1, 8)
                          if 7 >= (x + i) >= 0 and 7 >= (y - i) >= 0),
                     list(self.field[y + i][x - i] for i in range(1, 8)
                          if 7 >= (x - i) >= 0 and 7 >= (y + i) >= 0),
                     list(self.field[y - i][x - i] for i in range(1, 8)
                          if 7 >= (x - i) >= 0 and 7 >= (y - i) >= 0)]
            for lst in vars_:
                for btn in lst:
                    if btn.text() not in list(icons.values())[1::2]:
                        btn.setStyleSheet('background-color:gray')
                        if btn.text() in list(icons.values())[0::2]:
                            break
                        continue
                    break
        elif txt == icons['wp']:
            vars_ = list(self.field[y + j][x + i] for j, i in ((1, 0), (1, 1), (1, -1))
                         if 7 >= (x + i) >= 0 and 7 >= (y + i) >= 0)
            for btn in vars_:
                if (btn.text() not in list(icons.values())[0::2] and btn == vars_[0]) \
                        or (btn.text() in list(icons.values())[1::2] and btn != vars_[0]):
                    btn.setStyleSheet('background-color:gray')
        elif txt == icons['bp']:
            vars_ = list(self.field[y + j][x + i] for j, i in ((-1, 0), (-1, -1), (-1, 1))
                         if 7 >= (x + i) >= 0 and 7 >= (y + i) >= 0)
            for btn in vars_:
                if (btn.text() not in list(icons.values())[1::2] and btn == vars_[0]) \
                        or (btn.text() in list(icons.values())[0::2] and btn != vars_[0]):
                    btn.setStyleSheet('background-color:gray')

        if self.field[y][x].text() != '' and len(vars_) != 0:
            Store.starty = y
            Store.startx = x
            Store.txt = txt
        if self.field[y][x].palette().button().color().name() == '#808080':
            self.moveit(y, x)

    def moveit(self, y, x):
        h.colorize(self)
        print('ok', self.field[y][x].text())
        self.field[y][x].setText(Store.txt)
        self.field[Store.starty][Store.startx].setText('')


class Store:
    def __init__(self, x, y, txt):
        self.startx = x
        self.starty = y
        self.txt = txt


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Chess()
    ex.show()
    sys.exit(app.exec_())
