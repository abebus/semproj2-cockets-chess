def colorize(self):
    [self.field[i][j].setStyleSheet('background-color:#f2f2f2') for i in range(0, 8) for j in range(0, 8)
     if 7 >= i >= 0 and 7 >= j >= 0 and i % 2 == j % 2]
    [self.field[i][j].setStyleSheet('background-color: #404040') for i in range(0, 8) for j in range(0, 8)
     if 7 >= i >= 0 and 7 >= j >= 0 and i % 2 != j % 2]