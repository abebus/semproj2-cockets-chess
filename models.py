icons = {'bhorse':'♘','whorse':'♞','bking':'♚','wking':'♔','bqueen':'♕','wqueen':'♛','bp':'♙','wp':'♟','bl':'♖','wl':'♜','weleph':'♝','beleph':'♗'}
class Nofigure():
    btn.setText('')
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



#  figures = {'bhorse':(U+2658),'whorse':♞,'bking':♚,'wking':♔,'bqueen':♕,'wqueen':♛,'bp':♙,'wp':♟,'bl':♖,'wl':♜,'weleph':♝,'beleph':♗}

def filter_(lst):
    return list(filter(lambda i: 1 <= i[0] <= 8 and 1 <= i[1] <= 8, lst))


def vars_(lst, x, y):
    return list(map(lambda i: (x+i[0], y+i[1]), lst))


class Figure():
    def __init__(self, color, icon):
        self.color = color
        self.icon = icon

    def moves(self, x, y):
        pass

    def kill(self, x, y):
        return self.moves(x, y)


class Horse(Figure):
    def __init__(self,color,icon):
        super().__init__(color,icon)

    def moves(self, x, y):
        variants = [(2,1),(2,-1),(-2,-1),(-2,1),(1,2),(-1,-2),(-1,2),(1,-2)]
        vars = vars_(variants, x, y)
        filtered = filter_(vars)
        return filtered


class King(Figure):
    def __init__(self,color,icon):
        super().__init__(color,icon)

    def moves(self, x, y):
        variants = ((1,1),(1,-1),(-1,0),(1,0),(1,2),(-1,-2),(-1,2),(1,-2))
        vars = vars_(variants, x, y)
        filtered = filter_(vars)
        return filtered


class Queen(Figure):
    def __init__(self,color,icon):
        super().__init__(color,icon)

    def moves(self, x, y):
        variants = list()
        for i in range(1, 8):
            variants.append((i, 0))
            variants.append((0, i))
            variants.append((i, i))
            variants.append((-i, 0))
            variants.append((0, -i))
            variants.append((-i, -i))
            variants.append((-i, i))
            variants.append((i, -i))
        vars = vars_(variants, x, y)
        filtered = filter_(vars)
        return filtered


class Elephant(Figure):
    def __init__(self,color,icon):
        super().__init__(color,icon)

    def moves(self, x, y):
        variants = list()
        for i in range(1, 8):
            variants.append((i, i))
            variants.append((-i, -i))
            variants.append((-i, i))
            variants.append((i, -i))
        vars = vars_(variants, x, y)
        filtered = filter_(vars)
        return filtered


class Lada(Figure):
    def __init__(self,color,icon):
        super().__init__(color,icon)

    def moves(self, x, y):
        variants = list()
        for i in range(1, 8):
            variants.append((i, 0))
            variants.append((0, i))
            variants.append((-i, 0))
            variants.append((0, -i))
        vars = vars_(variants, x, y)
        filtered = filter_(vars)
        return filtered


class Pesh(Figure):
    def __init__(self,color,icon):
        super().__init__(color,icon)

    def moves(self, x, y):
        variants = ((1,0),)
        vars = vars_(variants, x, y)
        filtered = filter_(vars)
        return filtered

