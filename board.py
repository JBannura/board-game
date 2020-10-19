"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""

import pygame
from pygame import Rect
import random
import time
from network import Network

from button import Button

class Game:
    
    def __init__(self, width, height, margin, x_grid, y_grid):
        
        # Initialize pygame
        pygame.init()
        pygame.font.init()
        
        # Set title of screen
        pygame.display.set_caption("MaZe")
        
        # Criando o dado
        self.dice = [Button("Roll", 300, 77, (255, 255, 255))]
        
        # Dimensoes
        self.width  = width    
        self.height = height 
        self.margin = margin
        self.x_grid = x_grid
        self.y_grid = y_grid
        
        self.grid = []    
        self.player_list = []
    
    def create_screen(self, width, height):
        window_size = [width, height]
        self.screen = pygame.display.set_mode(window_size)
    
    def create_board(self):    
        for row in range(self.x_grid):
            # Add an empty array that will hold each cell in this row
            self.grid.append([])
            for column in range(self.y_grid):
                casa = Casa((self.margin + self.width) * column + self.margin,
                            (self.margin + self.height) * row + self.margin,
                            self.width,
                            self.height)
                casa.rect = Rect(casa.x1, casa.y1, casa.x2, casa.y2)
                self.grid[row].append(casa)  # Append a cell
    
    def add_player(self, player):
        self.player_list.append(player)
    
    def atualiza_posicao(self, posicao):
        self.actual = posicao    
    
    #def atualiza_janela(self, p1, p2):
    
    # Dice Roll
    def dice_roll(self):
        diceRoll = random.randint(1, 6)
        print(f"Rolou: {diceRoll}")
        return diceRoll
    
    def board_coloring(self):
        
        for row in range(self.x_grid):
            for column in range(self.y_grid):
                
                if column == 0 or column == 11 or row == 0 or row == 9:
                    casa = self.grid[row][column]
                    casa.color = (94, 191, 226)
                
                elif column == 2 and row != 8:    
                    casa = self.grid[row][column]
                    casa.color = (94, 191, 226)
                
                elif row == 7 and column != 1 and column != 10:
                    casa = self.grid[row][column]
                    casa.color = (94, 191, 226)
                
                elif column == 9 and row != 1 and row != 8:
                    casa = self.grid[row][column]
                    casa.color = (94, 191, 226)
                
                elif row == 2 and column != 1 and column != 3 and column != 10:
                    casa = self.grid[row][column]
                    casa.color = (94, 191, 226)
                
                elif column == 4 and row != 1 and row != 6 and row != 8:
                    casa = self.grid[row][column]
                    casa.color = (94, 191, 226)
                
                elif row == 5 and column != 1 and column != 3 and column != 8 and column != 10:
                    casa = self.grid[row][column]
                    casa.color = (94, 191, 226)
                
                elif row == 4 and column != 1 and column != 3 and column != 5 and column != 8 and column != 10:
                    casa = self.grid[row][column]
                    casa.color = (94, 191, 226)
        
    def create_path(self):
        self.path = []
        
        # 1: [1, 1] - [8, 1]
        for x in range(1, 9):
            self.path.append(self.grid[x][1])
        
        # 2: [8, 2] - [8, 10]
        for y in range(2, 11):
            self.path.append(self.grid[8][y])
        
        # 3: [7, 10] - [1, 10] 
        for x in range(7, 0, -1):
            self.path.append(self.grid[x][10])
        
        # 4: [1, 9] - [1, 3]
        for y in range(9, 2, -1):
            self.path.append(self.grid[1][y])
        
        # 5: [2, 3] - [6, 3]
        for x in range(2, 7):
            self.path.append(self.grid[x][3])
        
        # 6: [6, 4] - [6, 8]
        for y in range(4, 9):
            self.path.append(self.grid[6][y])
        
        # 7: [5, 8] - [3, 8]
        for x in range(5, 2, -1):
            self.path.append(self.grid[x][8])
        
        # 8: [3, 7] - [3, 5]
        for y in range(7, 4, -1):
            self.path.append(self.grid[3][y])
        
        # 9: [4, 5]
        self.path.append(self.grid[4][5])
        
        # Setando cores da posição inicial e final do tabuleiro
        self.path[-1].color  = (235, 203, 0)
        self.path[0].color = (164, 164, 164)
        
        """
        Board Design:   48 casas
                        24 casas com efeito
                        12 casas com efeito positivo
                        12 casas com efeito negativo

                        0 - casa neutra
                        1 - casa boa
                        2 - casa ruim
        """
        
        path_dict = {0: 0,
                    1: [1, 1],
                    2: 0,
                    3: [2, -1],
                    4: [1, 1],
                    5: 0,
                    6: 0,
                    7: [1, 4],
                    8: [2, -2],
                    9: [1, 1],
                    10: 0,
                    11: [2, -1],
                    12: 0,
                    13: [2, -1],
                    14: 0,
                    15: 0,
                    16: [2, -2],
                    17: 0,
                    18: [1, 1],
                    19: [2, -2],
                    20: 0,
                    21: [2, -1],
                    22: [1, 1],
                    23: 0,
                    24: 0,
                    25: [1, 1],
                    26: 0,
                    27: [1, 2],
                    28: [2, -1],
                    29: 0,
                    30: [1, 1],
                    31: 0,
                    32: [1, 1],
                    33: 0,
                    34: [2, -1],
                    35: [1, 1],
                    36: 0,
                    37: [2, -1],
                    38: 0,
                    39: [1, 1],
                    40: 0,
                    41: [2, -1],
                    42: 0,
                    43: 0,
                    44: [1, 1],
                    45: 0,
                    46: [2, -1],
                    47: 0}
                     
        for key in path_dict:
            
            
            try:
                if path_dict[key][0] == 1:
                    self.path[key].good_place()
                    self.path[key].effect(path_dict[key][1])
             
                elif path_dict[key][0] == 2:
                    self.path[key].bad_place()
                    self.path[key].effect(path_dict[key][1])    
            
            except:
                pass
class Casa:
    
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.id = 0
        self.color = (255, 255, 255)
        self.rect = ''
        
    def bad_place(self):
        self.id = 2
        self.color = (222, 43, 43)
    
    def good_place(self):
        self.id = 1
        self.color = (77, 235, 87)
    
    def effect(self, code):
        self.effect = code    