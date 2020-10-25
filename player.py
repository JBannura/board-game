class Player:
    
    def __init__(self, name, pos_x, pos_y):
        self.player = '>'
        self.name = name
        self.x = int(pos_x)
        self.y = int(pos_y)

        self.prev_x = self.x
        self.prev_y = self.y
        
        self.coord = [self.x, self.y]

        self.win = False
        
    def atualiza_posicao(self, pos_x, pos_y):
        self.x = int(pos_x)
        self.y = int(pos_y)
        self.coord = [self.x, self.y]
    