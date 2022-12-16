import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QGridLayout, QLabel, QVBoxLayout, \
    QHBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QObject, QSize
from chess_converted import Ui_MainWindow
from models import icons
from threading import Thread
from time import sleep

class EmojisWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EmojijLOLOL")
        self.main_grid = QGridLayout()
        self.setLayout(self.main_grid)
        self.emojis = []
        self.populate()
        self.logic()

    def populate(self):
        """
        можно ебануть сколько угодно смайликов
        :return:
        """
        row_width = 5
        row = 0
        column = 0
        for emoji in os.listdir('emojis'):
            btn = QPushButton()
            emoji_name = emoji.split('.')[0]
            btn.setObjectName(emoji_name)
            btn.setIcon(QIcon(f'emojis/{emoji}'))
            btn.setIconSize(QSize(60, 60))
            self.emojis.append(btn)
            self.main_grid.addWidget(btn, column, row)
            if row < row_width - 1:
                row += 1
            else:
                row = 0
                column += 1

    def logic(self):
        for btn in self.emojis:
            btn.clicked.connect(lambda state, button=btn: self.picked_emoji_is(button))

    @pyqtSlot()
    def picked_emoji_is(self, btn):
        return btn

class LobbySelectorWidnow(QWidget):
    def __init__(self):
        super().__init__()
        ...


class Chess(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        font = QFont()
        font.setFamily(u'Arial')  # шрифт
        font.setPointSize(12)  # размер шрифта
        QMainWindow.setFont(self, font)
        self.setFixedSize(653, 370)  # фиксированный размер окна
        self.ui.gridLayout.setSpacing(0)  # ставим кнопки(клетки) в гриде вплотную

        # удобно обращаемся к клеточкам
        self.field = [
            [self.ui._11, self.ui._21, self.ui._31, self.ui._41, self.ui._51, self.ui._61, self.ui._71, self.ui._81],
            [self.ui._12, self.ui._22, self.ui._32, self.ui._42, self.ui._52, self.ui._62, self.ui._72, self.ui._82],
            [self.ui._13, self.ui._23, self.ui._33, self.ui._43, self.ui._53, self.ui._63, self.ui._73, self.ui._83],
            [self.ui._14, self.ui._24, self.ui._34, self.ui._44, self.ui._54, self.ui._64, self.ui._74, self.ui._84],
            [self.ui._15, self.ui._25, self.ui._35, self.ui._45, self.ui._55, self.ui._65, self.ui._75, self.ui._85],
            [self.ui._16, self.ui._26, self.ui._36, self.ui._46, self.ui._56, self.ui._66, self.ui._76, self.ui._86],
            [self.ui._17, self.ui._27, self.ui._37, self.ui._47, self.ui._57, self.ui._67, self.ui._77, self.ui._87],
            [self.ui._18, self.ui._28, self.ui._38, self.ui._48, self.ui._58, self.ui._68, self.ui._78, self.ui._88]]

        self.construct_field()

        self.color_field()
        self.test()
        self.emoji_window = EmojisWindow()
        self.show_emojis()

        # гуи парсит ютфные символы фигур и ставит картинку на кнопку
        # raster_demon = Thread(daemon=True, target=self.raster_figure)
        # raster_demon.start()

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

    def color_field(self):
        for row_i in range(len(self.field)):
            for btn_j in range(len(self.field)):
                if (row_i + btn_j) % 2 != 0:
                    self.field[row_i][btn_j].setStyleSheet("background-color: white")
                else:
                    self.field[row_i][btn_j].setStyleSheet("background-color: darkGreen")

    @pyqtSlot()
    def test(self):
        for row in self.field:
            for btn in row:
                btn.clicked.connect(lambda state, x=btn: print(x.objectName()))

    @pyqtSlot()
    def show_emojis(self):
        self.ui.btn_emojis.clicked.connect(self.emoji_window.show)

    @pyqtSlot()
    def raster_figure(self):
        while True:
            for row in self.field:
                for btn in row:
                    for k, v in icons.items():
                        if btn.text() == v:
                            btn.setIcon(QIcon(f"chess_img/{k}.png"))
                            btn.setIconSize(QSize(32, 32))
                            # btn.setText('')
                        if btn.text() == '':
                            btn.setIcon(QIcon(None))
            sleep(1)
            ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Chess()
    ex.show()
    sys.exit(app.exec_())
