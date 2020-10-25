import player
from termcolor import colored as c
import os
os.system('color')

class Board:
    
    def __init__(self, p1, p2):
        
        self.board = self.create_board()
        self.p1 = p1
        self.p2 = p2
        
    def create_board(self):
        
        matrix = []
        line = []
        
        for i in range (0, 4):
            line = []
            for j in range(0, 50):
                
                if i == 0 or i == 3:
                    line.append(c('♠', 'green'))
                
                elif (i == 1 or i == 2) and (j == 49):
                    line.append('#')
                
                else:
                    line.append(c(0, 'yellow'))

                
            matrix.append(line) 

        return matrix
    
    def player_in_board(self):
        
        # print(f"Player 1 positions: x -> {self.p1.x}    y -> {self.p1.y}")
        # print(f"Player 2 positions: x -> {self.p2.x}    y -> {self.p2.y}\n")
        
        if self.p1.y > 49:
            self.p1.y = 49
            self.p1.win = True
            
        elif self.p2.y > 49:
            self.p2.y = 49
            self.p2.win = True
            
        self.board[self.p1.prev_x][self.p1.prev_y] = c(0, 'yellow')
        self.board[self.p2.prev_x][self.p2.prev_y] = c(0, 'yellow')
        
        self.board[self.p1.x][self.p1.y] = c(self.p1.player, 'cyan')
        self.board[self.p2.x][self.p2.y] = c(self.p2.player, 'red')
        
        self.p1.prev_x = self.p1.x
        self.p1.prev_y = self.p1.y
        self.p2.prev_x = self.p2.x
        self.p2.prev_y = self.p2.y
        
    def print_board(self): 
    
        for line in self.board:
            for casa in line:
                print(casa, end='')
            
            print()
        
        print()
        
    def refresh(self):
        self.player_in_board()
        self.print_board()
    
if __name__ == "__main__":
    
    p1 = player.Player(1, 0)
    p2 = player.Player(2, 0)
    
    board = Board(p1, p2)
    board.refresh()
    
    board.p1.x = 1
    board.p1.y = 5
    
    board.p2.x = 2
    board.p2.y = 5
    
    board.refresh()