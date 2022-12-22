import sys
import socket
import pickle
import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject, QThread
from chess_gui import *
from models import icons
import helper as h


class BackendClient(QThread):
    address = ("127.0.0.1", 10000)

    def __init__(self, chat_signal,varsignal, go_signal, end, name):
        super().__init__()
        self.name = name
        self.chsignal = chat_signal
        self.varsignal = varsignal
        self.gosignal = go_signal
        self.end = end

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(BackendClient.address)

    def run(self):
        while 1:
            binary_data = self.sock.recv(1024)
            if binary_data is None or not len(binary_data):
                break
            info = pickle.loads(binary_data)
            print('info:', info)
            if len(info) == 1:
                text = info.get('text')
                self.chsignal.emit(text)
            elif len(info) == 2:
                text = info.get('text')
                self.end.emit((text,),'','')
            elif len(info) == 3:
                x = info.get('x')
                y = info.get('y')
                color = info.get('color')
                self.varsignal.emit(y, x, color)
            elif len(info) == 6:
                a = info.get('a')
                b = info.get('b')
                y = info.get('y')
                x = info.get('x')
                txt = info.get('txt')
                color = info.get('color')
                self.gosignal.emit(a, b, y, x, txt, color)

    def send(self, *args):
        print('len args:', len(args), args)
        if len(args) == 1:
            protocol = {"text": args[0]}
            self.sock.send(pickle.dumps(protocol))
        elif len(args) == 2:
            protocol = {"y": args[0], "x": args[1]}
            self.sock.send(pickle.dumps(protocol))
        elif len(args) == 3:
            protocol = {"text": args[0][0], " ": "", "": ""}
            self.sock.send(pickle.dumps(protocol))
        elif len(args) == 5:
            protocol = {"a": args[0], "b": args[1],
                        "y": args[2], "x": args[3],
                        "txt": args[4]}
            self.sock.send(pickle.dumps(protocol))


class Communication(QObject):
    pre_vars_signal = pyqtSignal(int, int)
    vars_signal = pyqtSignal(int, int, int)
    msg_signal = pyqtSignal(str)
    move_signal = pyqtSignal(int, int, int, int, str, int)
    end = pyqtSignal(tuple, str, str)


class Chess(Chess):
    # global startx
    # global starty
    def __init__(self):
        super().__init__()
        self.a = 0
        self.b = 0
        self.c = 0
        self.comm = Communication()
        self.name = 'user'
        self.comm.vars_signal.connect(self.variants)
        self.comm.msg_signal.connect(self.recv_msg)
        self.comm.move_signal.connect(self.moveit)
        self.comm.pre_vars_signal.connect(self.pre_vars)
        self.comm.end.connect(self.end_game)
        self.client = BackendClient(self.comm.msg_signal, self.comm.vars_signal, self.comm.move_signal, self.comm.end, self.name)
        self.client.start()
        self.logic()
        for lst in range(len(self.field)):
            for btn in range(len(self.field[lst])):
                self.field[lst][btn].clicked.connect(lambda state, x=btn, y=lst: self.pre_vars(y, x))

    def logic(self):
        self.findChild(QPushButton, 'btn_send_msg').clicked.connect(self.send_msg)
        self.ui.chat_history.setText(f"Welcome {self.name}")

    @pyqtSlot(str)
    def recv_msg(self, text):
        self.ui.chat_history.append(text)

    def send_msg(self):
        text: str = self.ui.lineEdit_2.text()
        if len(text.strip()) > 0:
            self.ui.lineEdit_2.setText("")
            self.client.send(text)

    @pyqtSlot(int, int)
    def pre_vars(self, y, x):
        self.client.send(y, x)

    @pyqtSlot(int, int, int)
    def variants(self, y, x, color):
        if self.field[y][x].palette().button().color().name() == '#808080' and color == 0 and self.field[y][x].text() in list(icons.values())[1::2]:
            self.client.send(self.a, self.b, y, x, self.c)
        if self.field[y][x].palette().button().color().name() == '#808080' and color == 1 and self.field[y][x].text() in list(icons.values())[0::2]:
            self.client.send(self.a, self.b, y, x, self.c)
        if self.field[y][x].text() != '':
            h.colorize(self)
        vars_ = []
        txt = self.field[y][x].text()
        if color == 0:
            if txt == icons['wking']:
                vars_ = list(self.field[y + j][x + i] for j, i in
                             ((1, 1), (1, 0), (1, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1))
                             if 7 >= (y + j) >= 0 and 7 >= (x + i) >= 0)
                for btn in vars_:
                    if btn.text() not in list(icons.values())[0::2]:
                        btn.setStyleSheet('background-color:gray')
            elif txt == icons['whorse']:
                vars_ = list(self.field[y + j][x + i] for j, i in
                             ((2, 1), (-2, 1), (1, -2), (1, 2), (-2, -1), (2, -1), (-1, 2), (-1, -2))
                             if 7 >= (y + j) >= 0 and 7 >= (x + i) >= 0)
                for btn in vars_:
                    if btn.text() not in list(icons.values())[0::2]:
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
            elif txt == icons['wp']:
                vars_ = list(self.field[y + j][x + i] for j, i in ((1, 0), (1, 1), (1, -1))
                             if 7 >= (x + i) >= 0 and 7 >= (y + i) >= 0)
                for btn in vars_:
                    if (btn.text() not in list(icons.values())[0::2] and btn.text() == "" and btn == vars_[0]) \
                            or (btn.text() in list(icons.values())[1::2] and btn != vars_[0]):
                        btn.setStyleSheet('background-color:gray')
        else:
            if txt == icons['bking']:
                vars_ = list(self.field[y + j][x + i] for j, i in
                             ((1, 1), (1, 0), (1, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1))
                             if 7 >= (y + j) >= 0 and 7 >= (x + i) >= 0)
                for btn in vars_:
                    if btn.text() not in list(icons.values())[1::2]:
                        btn.setStyleSheet('background-color:gray')
            elif txt == icons['bhorse']:
                vars_ = list(self.field[y + j][x + i] for j, i in
                             ((2, 1), (-2, 1), (1, -2), (1, 2), (-2, -1), (2, -1), (-1, 2), (-1, -2))
                             if 7 >= (y + j) >= 0 and 7 >= (x + i) >= 0)
                for btn in vars_:
                    if btn.text() not in list(icons.values())[1::2]:
                        btn.setStyleSheet('background-color:gray')
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
            elif txt == icons['bp']:
                vars_ = list(self.field[y + j][x + i] for j, i in ((-1, 0), (-1, -1), (-1, 1))
                             if 7 >= (x + i) >= 0 and 7 >= (y + i) >= 0)
                for btn in vars_:
                    if (btn.text() not in list(icons.values())[1::2] and btn == vars_[0]) \
                            or (btn.text() in list(icons.values())[0::2] and btn != vars_[0]):
                        btn.setStyleSheet('background-color:gray')
        if self.field[y][x].text() != '' and len(vars_) != 0:
            self.a = y
            self.b = x
            self.c = txt
        if self.field[y][x].palette().button().color().name() == '#808080' and self.field[y][x].text() == "" \
                and color == 0 and self.field[self.a][self.b].text() in list(icons.values())[0::2]:
            self.client.send(self.a, self.b, y, x, self.c)
        if self.field[y][x].palette().button().color().name() == '#808080' and self.field[y][x].text() == "" \
                and color == 1 and self.field[self.a][self.b].text() in list(icons.values())[1::2]:
            self.client.send(self.a, self.b, y, x, self.c)

    @pyqtSlot(int, int, int, int, str, int)
    def moveit(self, a, b, y, x, txt, color):
        h.colorize(self)
        if self.field[y][x].text() in list(icons.values())[2:4]:
            self.client.send((self.field[y][x].text(),), '', '')
        if txt in list(icons.values())[0::2] and color == 0:
            self.field[y][x].setText(txt)
            self.field[a][b].setText('')
            return 0
        elif txt in list(icons.values())[1::2] and color == 1:
            self.field[y][x].setText(txt)
            self.field[a][b].setText('')
            return 0
        else:
            return 0

    @pyqtSlot(tuple, str, str)
    def end_game(self,tup):
        txt = tup[0]
        for lst in range(len(self.field)):
            for btn in range(len(self.field[lst])):
                self.field[lst][btn].setText("")
                h.construct_field(self)
        if txt == list(icons.values())[2]:
            self.client.send('User2 wins')
        elif txt == list(icons.values())[3]:
            self.client.send('User1 wins')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Chess()
    ex.show()
    sys.exit(app.exec_())
