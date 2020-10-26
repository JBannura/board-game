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
                
                """
                elif (i == 1 or i == 2) and ((j == 6) or (j == 10) or (j == 20) or (j == 31) or (j == 39) or (j == 45)):
                    line.append(c('0', 'red'))

                elif (i == 1 or i == 2) and ((j == 3) or (j == 15) or (j == 24) or (j == 28) or (j == 35) or (j == 41)):
                    line.append(c('0', 'green'))
                
                """
                
                if i == 0 or i == 3:
                    casa = Casa(i, j, '♠', 'blue')
                    line.append(casa)
                
                elif (i == 1 or i == 2) and ((j == 6) or (j == 10) or (j == 20) or (j == 31) or (j == 39) or (j == 45)):
                    casa = Casa(i, j, '0', 'red')
                    line.append(casa)

                elif (i == 1 or i == 2) and ((j == 3) or (j == 15) or (j == 24) or (j == 28) or (j == 35) or (j == 41)):
                    casa = Casa(i, j, '0', 'green')
                    line.append(casa)
                
                elif (i == 1 or i == 2) and (j == 49):
                    casa = Casa(i, j, '#', 'yellow')
                    line.append(casa)
                
                else:
                    casa = Casa(i, j, '0', 'white')
                    line.append(casa)
                
            matrix.append(line) 

        return matrix
    
    def player_in_board(self):
        
        # print(f"Player 1 positions: x -> {self.p1.x}    y -> {self.p1.y}")
        # print(f"Player 2 positions: x -> {self.p2.x}    y -> {self.p2.y}\n")
        
        if self.p1.y > 49:
            self.p1.y = 49
            self.p1.win = True
            
        if self.p2.y > 49:
            self.p2.y = 49
            self.p2.win = True
            
        self.board[self.p1.prev_x][self.p1.prev_y].colored_icon = c(0, self.board[self.p1.prev_x][self.p1.prev_y].color)
        self.board[self.p2.prev_x][self.p2.prev_y].colored_icon = c(0, self.board[self.p1.prev_x][self.p1.prev_y].color)
        
        if self.board[self.p1.x][self.p1.y].color == 'red':
            print("Você caiu em uma casa vermelha! Volte uma posição")
            self.p1.y -= 1
        
        elif self.board[self.p1.x][self.p1.y].color == 'green':
            print("Você caiu em uma casa verde! Avance uma posição" )
            self.p1.y += 1
        
        if self.board[self.p2.x][self.p2.y].color == 'red':
            self.p2.y -= 1
        
        elif self.board[self.p2.x][self.p2.y].color == 'green':
            self.p2.y += 1
            
        self.board[self.p1.x][self.p1.y].colored_icon = c(self.p1.player, 'cyan')
        self.board[self.p2.x][self.p2.y].colored_icon = c(self.p2.player, 'magenta')
        
        self.p1.prev_x = self.p1.x
        self.p1.prev_y = self.p1.y
        self.p2.prev_x = self.p2.x
        self.p2.prev_y = self.p2.y
        
    def print_board(self): 
    
        for line in self.board:
            for casa in line:
                print(casa.colored_icon, end='')
            
            print("\n")
        
        print()
        
    def refresh(self):
        self.player_in_board()
        self.print_board()
    
class Casa:
    
    def __init__(self, i, j, icon, color):
        self.i = i
        self.j = j
        self.icon = icon
        self.color = color
        self.colored_icon = c(icon, color)
        
    #     if self.color == 'red':
    #         self.bad_place()
        
    #     elif self.color == 'green':
    #         self.good_place()
            
    # def bad_place(self):    
    #     self.effect = -1
    
        
    # def good_place(self):
    #     self.effect = 1
    
if __name__ == "__main__":
    
    p1 = player.Player('', 1, 0)
    p2 = player.Player('', 2, 0)
    
    board = Board(p1, p2)
    board.refresh()
    
    board.p1.x = 1
    board.p1.y = 3
    
    board.p2.x = 2
    board.p2.y = 3
    
    board.refresh()
    
    board.p1.x = 1
    board.p1.y = 6
    
    board.p2.x = 2
    board.p2.y = 6
    
    board.refresh()
    