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
        diceRoll = random.randint(1, 1)
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
        
        dict_ = {}
        for index in range(0, 24):
            
            casa = random.randint(1, 46)
    
            if len(dict_) > 0:
                try:
                    if casa in dict_:
                        while casa in dict_:
                            casa = random.randint(1, 46)
                        
                except KeyError:
                    pass
                
            if index >= 12:
                self.path[casa].bad_place()
            
            else:
                self.path[casa].good_place()
            
            dict_[casa] = casa

class Casa:
    
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.color = (255, 255, 255)
        self.rect = ''
        
    def bad_place(self):
        self.color = (222, 43, 43)
    
    def good_place(self):
        self.color = (77, 235, 87)