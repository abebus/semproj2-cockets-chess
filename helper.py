from models import icons
def colorize(self):
    [self.field[i][j].setStyleSheet('background-color:#f2f2f2') for i in range(0, 8) for j in range(0, 8)
     if 7 >= i >= 0 and 7 >= j >= 0 and i % 2 == j % 2]
    [self.field[i][j].setStyleSheet('background-color: #404040') for i in range(0, 8) for j in range(0, 8)
     if 7 >= i >= 0 and 7 >= j >= 0 and i % 2 != j % 2]
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