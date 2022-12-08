#список ходов выводится в консоль для каждой белой фигуры (кроме коня и пешки)
#реализован метод перемещения фигуры по одному из возможных маршрутов
#в консоль выводится двумерный список - первый список возможных ходов, второй - кого можно съесть
#фигуры можно есть

import random
import itertools

class Side:
    white = 0
    black = 1
    none = 2

class Figure:
    def __init__(self, side):
        self.side = side
        type = None
    def __str__(self):
        return self.type[0 if self.side == Side.white else 1]


class Pawn(Figure):
    type = ('pw ', 'pb ')
    def moves(self, field, x, y):
        moves = []
        if self.side == Side.white and y < 7 and field.whatside(x, y+1) == Side.none:
            moves.append([x, y+1])
        return moves

class King(Figure):
    type = ('kw ', 'kb ')
    def moves(self, field, x, y):
        moves = []
        attacks = []
        #down
        if self.side == Side.white and y < 7 and (field.whatside(x, y+1) == Side.none):
            moves.append([x, y+1])
        if self.side == Side.white and y < 7 and (field.whatside(x, y+1) == Side.black):
            attacks.append([x, y+1])

        #right
        if self.side == Side.white and x < 7 and field.whatside(x+1, y) == Side.none:
            moves.append([x+1, y])
        if self.side == Side.white and x < 7 and (field.whatside(x+1, y) == Side.black):
            attacks.append([x+1, y])

        #right-down
        if self.side == Side.white and (x < 7 and y < 7) and field.whatside(x+1, y+1) == Side.none:
            moves.append([x+1, y+1])
        if self.side == Side.white and (y < 7 and x < 7) and (field.whatside(x+1, y+1) == Side.black):
            attacks.append([x+1, y+1])
        #left
        if self.side == Side.white and x > 0 and field.whatside(x-1, y) == Side.none:
            moves.append([x-1, y])
        if self.side == Side.white and x > 0 and (field.whatside(x-1, y) == Side.black):
            attacks.append([x-1, y])
        #up
        if self.side == Side.white and y > 0 and field.whatside(x, y-1) == Side.none:
            moves.append([x, y-1])
        if self.side == Side.white and y > 0 and (field.whatside(x, y-1) == Side.black):
            attacks.append([x, y-1])
        #left-up
        if self.side == Side.white and (x > 0 and y > 0) and field.whatside(x-1, y-1) == Side.none:
            moves.append([x-1, y-1])
        if self.side == Side.white and (x > 0 and y > 0) and (field.whatside(x-1, y-1) == Side.black):
            attacks.append([x-1, y-1])
        #left-down
        if self.side == Side.white and (x > 0 and y < 7) and field.whatside(x-1, y+1) == Side.none:
            moves.append([x-1, y+1])
        if self.side == Side.white and (x > 0 and y < 7) and (field.whatside(x-1, y+1) == Side.black):
            attacks.append([x-1, y+1])
        #right-up
        if self.side == Side.white and (x < 7 and y > 0) and field.whatside(x+1, y-1) == Side.none:
            moves.append([x+1, y-1])
        if self.side == Side.white and (x < 7 and y > 0) and (field.whatside(x+1, y-1) == Side.black):
            attacks.append([x+1, y-1])
        return moves, attacks
class Horse(Figure):
    type = ('hw ', 'hb ')
    def moves(self, field, x, y):
        pass
class Rook(Figure):
    type = ('rw ', 'rb ')
    def moves(self, field, x, y):
        moves = []
        attacks = []
        #down
        i = 1
        while self.side == Side.white and y+i <= 7 and (field.whatside(x, y+i) == Side.none or field.whatside(x, y+i) == Side.black):
            if field.whatside(x, y+i) == Side.none:
                moves.append([x, y+i])
            if field.whatside(x, y+i) == Side.black:
                attacks.append([x, y+i])
                break
            i+=1
        #up
        j = 1
        while self.side == Side.white and y-j >= 0 and (field.whatside(x, y-j) == Side.none or field.whatside(x, y-j) == Side.black):
            if field.whatside(x, y-j) == Side.none:
                moves.append([x, y-j])
            if field.whatside(x, y-j) == Side.black:
                attacks.append([x, y-j])
                break
            j+=1
        #right
        k = 1
        while self.side == Side.white and x+k <= 7 and (field.whatside(x+k, y) == Side.none or field.whatside(x+k, y) == Side.black):
            if field.whatside(x+k, y) == Side.none:
                moves.append([x+k, y])
            if field.whatside(x+k, y) == Side.black:
                attacks.append([x+k, y])
                break
            k+=1
        #left
        q = 1
        while self.side == Side.white and x-q >= 0 and (field.whatside(x-q, y) == Side.none or field.whatside(x-q, y) == Side.black):
            if field.whatside(x-q, y) == Side.none:
                moves.append([x-q, y])
            if field.whatside(x-q, y) == Side.black:
                attacks.append([x-q, y])
                break
            q+=1
        return moves, attacks
class Queen(Figure):
    type = ('qw ', 'qb ')
    def moves(self, field, x, y):
        moves = []
        attacks = []
        #down
        m = 1
        while self.side == Side.white and y+m <= 7 and (field.whatside(x, y+m) == Side.none or field.whatside(x, y+m) == Side.black):
            if field.whatside(x, y+m) == Side.none:
                moves.append([x, y+m])
            if field.whatside(x, y+m) == Side.black:
                attacks.append([x, y+m])
                break
            m+=1
        #up
        p = 1
        while self.side == Side.white and y-p >= 0 and (field.whatside(x, y-p) == Side.none or field.whatside(x, y-p) == Side.black):
            if field.whatside(x, y-p) == Side.none:
                moves.append([x, y-p])
            if field.whatside(x, y-p) == Side.black:
                attacks.append([x, y-p])
                break

            p+=1
        #right
        c = 1
        while self.side == Side.white and x+c <= 7 and (field.whatside(x+c, y) == Side.none or field.whatside(x+c, y) == Side.black):
            if field.whatside(x+c, y) == Side.none:
                moves.append([x+c, y])
            if field.whatside(x+c, y) == Side.black:
                attacks.append([x+c, y])
                break
            c+=1
        #left
        a = 1
        while self.side == Side.white and x-a >= 0 and (field.whatside(x-a, y) == Side.none or field.whatside(x-a, y) == Side.black):
            if field.whatside(x-a, y) == Side.none:
                moves.append([x-a, y])
            if field.whatside(x-a, y) == Side.black:
                attacks.append([x-a, y])
                break

            a+=1
        #right-down
        h = 1
        while self.side == Side.white and (x+h <= 7 and y+h <= 7) and (field.whatside(x+h, y+h) == Side.none or field.whatside(x+h, y+h) == Side.black):
            if field.whatside(x+h, y+h) == Side.none:
                moves.append([x+h, y+h])
            if field.whatside(x+h, y+h) == Side.black:
                attacks.append([x+h, y+h])
                break
            h+=1
        #left-up
        g = 1
        while self.side == Side.white and (x-g >= 0 and y-g >= 0) and (field.whatside(x-g, y-g) == Side.none or field.whatside(x-g, y-g) == Side.black):
            if field.whatside(x-g, y-g) == Side.none:
                moves.append([x-g, y-g])
            if field.whatside(x-g, y-g) == Side.black:
                attacks.append([x-g, y-g])
                break
            g+=1
        f = 1
        #left-down
        while self.side == Side.white and (x-f >= 0 and y+f <= 7) and (field.whatside(x-f, y+f) == Side.none or field.whatside(x-f, y+f) == Side.black):
            if field.whatside(x-f, y+f) == Side.none:
                moves.append([x-f, y+f])
            if field.whatside(x-f, y+f) == Side.black:
                attacks.append([x-f, y+f])
                break
            f+=1
        #right-up
        p = 1
        while self.side == Side.white and (x+p <= 7 and y-p >= 0) and (field.whatside(x+p, y-p) == Side.none or field.whatside(x+p, y-p) == Side.black):
            if field.whatside(x+p, y-p) == Side.none:
                moves.append([x+p, y-p])
            if field.whatside(x+p, y-p) == Side.black:
                attacks.append([x+p, y-p])
                break
            p+=1
        return moves, attacks
class Bishop(Figure):
    type = ('bw ', 'bb ')
    def moves(self, field, x, y):
        moves = []
        attacks = []
        #right-down
        z = 1
        while self.side == Side.white and (x+z <= 7 and y+z <= 7) and (field.whatside(x+z, y+z) == Side.none or field.whatside(x+z, y+z) == Side.black):
            if field.whatside(x+z, y+z) == Side.none:
                moves.append([x+z, y+z])
            if field.whatside(x+z, y+z) == Side.black:
                attacks.append([x+z, y+z])
                break
            z+=1
        #left-up
        l = 1
        while self.side == Side.white and (x-l >= 0 and y-l >= 0) and (field.whatside(x-l, y-l) == Side.none or field.whatside(x-l, y-l) == Side.black):
            if field.whatside(x-l, y-l) == Side.none:
                moves.append([x-l, y-l])
            if field.whatside(x-l, y-l) == Side.black:
                attacks.append([x-l, y-l])
                break
            l+=1
        n = 1
        #left-down
        while self.side == Side.white and (x-n >= 0 and y+n <= 7) and (field.whatside(x-n, y+n) == Side.none or field.whatside(x-n, y+n)):
            if field.whatside(x-n, y+n) == Side.none:
                moves.append([x-n, y+n])
            if field.whatside(x-n, y+n) == Side.black:
                attacks.append([x-n, y+n])
                break
            n+=1
        #right-up
        b = 1
        while self.side == Side.white and (x+b <= 7 and y-b >= 0) and (field.whatside(x+b, y-b) == Side.none or field.whatside(x+b, y-b) == Side.black):
            if field.whatside(x+b, y-b) == Side.none:
                moves.append([x+b, y-b])
            if field.whatside(x+b, y-b) == Side.black:
                attacks.append([x+b, y-b])
                break
            b+=1
        return moves, attacks
class Nofigure:
    side = Side.none
    def moves(self, field, x, y):
        raise Exception('no figure')
    def __str__(self):
        return '      '


class Field:
    def __init__(self):
        self.field = [[Nofigure()]*8 for i in range(8)]
        # Spawner.
        for i in range(2):
            k = 0
            for j in range(pawns):
                count = pawns
                x, y = Field.freecell(self, j, i, count)
                self.field[x][y] = Pawn(i)
            for j in range(pawns*2, pawns*2+1):
                count = 1
                x, y = Field.freecell(self, j, i, count)
                self.field[x][y] = King(i)
            for j in range(pawns*2+2, pawns*2+2+horses):
                count = horses
                x, y = Field.freecell(self, j, i, count)
                self.field[x][y] = Horse(i)
            for j in range(pawns*2+2+horses*2, pawns*2+2+horses*2+rooks):
                count = rooks
                x, y = Field.freecell(self, j, i, count)
                self.field[x][y] = Rook(i)
            for j in range(pawns*2+2+horses*2+rooks*2, pawns*2+2+horses*2+rooks*2+bishops):
                count = bishops
                x, y = Field.freecell(self, j, i, count)
                self.field[x][y] = Bishop(i)
            for j in range(pawns*2+2+horses*2+rooks*2+bishops*2, pawns*2+2+horses*2+rooks*2+bishops*2+queens):
                count = queens
                x, y = Field.freecell(self, j, i, count)
                self.field[x][y] = Queen(i)

    def moves(self, x, y):
        return self.field[y][x].moves(self, x, y)
    def attack(self, x, y):
        return self.field[y][x].attack(self, x, y)

    def whatside(self, x, y):
        return self.field[y][x].side
    def whattype(self, x, y):
        return self.field[y][x].type

    def movefigure(self, xystart, xyfinish):
        self.field[xyfinish[1]][xyfinish[0]] = self.field[xystart[1]][xystart[0]]
        self.field[xystart[1]][xystart[0]] = Nofigure()

    def freecell(self, j, i, count):
        if i == 0:
            return results[j]
        else:
            return results[j+count]

    def whatisit(self):
        for i in range(8):
            for j in range(8):
                if a.whatside(i, j) != Side.none and a.whatside(i, j) == Side.white:
                    print(a.whattype(i, j), a.moves(i, j))


    def visualise(self):
        import tkinter as tk
        window = tk.Tk()
        for i in range(9):
            for j in range(9):
                frame = tk.Frame(
                    master=window,
                    relief=tk.RAISED,
                    borderwidth=1
                )
                frame.grid(row=i, column=j, sticky='nsew')
                if (j % 2 == 0 and i % 2 == 0 or j % 2 != 0 and i % 2 != 0) or i == 8 or j == 8:
                    bgcolor = 'brown'
                else:
                    bgcolor = 'yellow'
                if j == 8 and i != 8:
                    text_ = ' ' + str(8 - i) + ' '
                elif i == 8:
                    alphabet = (' A  ', ' B  ', ' C  ', ' D  ', ' E  ', ' F  ', ' G  ', ' H  ', '    ')
                    text_ = alphabet[j]
                else:
                    text_ = self.field[i][j]
                label = tk.Label(master=frame, text=text_, bg=bgcolor, font=('Roboto', 32))
                label.pack()
        window.mainloop()


    def __str__(self):
        first = ''
        for i in range(8):
            first += ''.join(map(str, self.field[i])) + "\n"
        return first

numbers = [0, 1, 2, 3, 4, 5, 6, 7]
results = list(itertools.permutations(numbers, 2))
random.shuffle(results)
pawns = random.randrange(8)
horses = random.randrange(2)
rooks = random.randrange(2)
bishops = random.randrange(2)
queens = 1
print(pawns, horses, rooks, bishops, queens)


print(Field())
a = Field()
a.whatisit()
Field().visualise()

#m = a.moves(1, 1)
#a.movefigure((1, 1), m[0])

#a.visualise()
