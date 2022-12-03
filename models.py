from chess import Ui_MainWindow

figures = {'bhorse':♘,'whorse':♞,'bking':♚,'wking':♔,'bqueen':♕,'wqueen':♛,'bp':♙,'wp':♟,'bl':♖,'wl':♜,'weleph':♝,'beleph':♗}

class Nofigure():
    side = Side.none
    def moves(self, field, x, y):
        raise Exception('no figure')

class Field:
    def __init__(self):
        self.field = [[Nofigure()]*8 for i in range(8)]

    def moves(self, x, y):
        return self.field[y][x].moves(self, x, y)

    def attack(self, x, y):
        return self.field[y][x].attack(self, x, y)

    def movefigure(self, xystart, xyfinish):
        self.field[xyfinish[1]][xyfinish[0]] = self.field[xystart[1]][xystart[0]]
        self.field[xystart[1]][xystart[0]] = Nofigure()

    def whatside(self, x, y):
        return self.field[y][x].side

    def whattype(self, x, y):
        return self.field[y][x].type
