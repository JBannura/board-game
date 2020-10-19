"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
import random
import time
from network import Network

from pygame import Rect

class Game:
    
    def __init__(self, width, height, margin, x_grid, y_grid):
        
        # Initialize pygame
        pygame.init()
        pygame.font.init()
        
        # Set title of screen
        pygame.display.set_caption("Array Backed Grid")
        
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
    
    def read_pos(self, str_):
        print(str_)
        str_ = str_.split(",")
        return int(str_[0]), int(str_[1])

    def make_pos(self, tup):
        print("make pos: ", str(tup[0]) + "," + str(tup[1]))
        return str(tup[0]) + "," + str(tup[1])

class Button:
    
    # Button creation
    def __init__(self, text, x, y, color):
        
        self.button_text   = text 
        self.button_x      = x
        self.button_y      = y
        self.button_color  = color
        self.button_width  = 50
        self.button_height = 35
    
    # Draw button
    def draw(self, screen):
        pygame.draw.rect(screen, self.button_color, (self.button_x, self.button_y, self.button_width, self.button_height)) 
        font = pygame.font.SysFont('comicsans', 20)
        text = font.render(self.button_text, 1, (0, 0, 0))
        screen.blit(text, (self.button_x + int(self.button_width/2) - int(text.get_width()/2), self.button_y + int(self.button_height/2) - int(text.get_height()/2)))

    # Dice click
    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        
        if (self.button_x <= x1 <= self.button_x + self.button_width) and (self.button_y <= y1 <= self.button_y + self.button_height):
            return True
        
        else:
            return False

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

class Player:
    
    def __init__(self, player_id, casa, play):
        
        self.width  = 3
        self.height = 3
        self.play   = play
        
        if player_id == '0':    
            self.color = (0, 0, 0)
            self.player_id = 1
            
            print(f"Center      : {casa.rect.center}")
    
            self.center = casa.rect.center
            self.player_rect = Rect(casa.x1, casa.y1, self.width, self.height)
            self.player_rect.center = casa.rect.center
            self.player_rect.center = (self.player_rect.center[0], int(self.player_rect.center[1] - 5))
            
            print(f"Player 1 Center: {self.player_rect.center}")
            
        elif player_id == '1':
            self.color = (188, 51, 215)
            self.player_id = 2
            
            print(f"Center      : {casa.rect.center}")
    
            self.center = casa.rect.center
            self.player_rect = Rect(casa.x1, casa.y1, self.width, self.height)
            self.player_rect.center = casa.rect.center
            self.player_rect.center = (self.player_rect.center[0], int(self.player_rect.center[1] + 5)) 
            
            print(f"Player 2 Center: {self.player_rect.center}")
            
        self.posicao_atual = 0
        self.message()
        
    def atualiza_posicao(self, resultado, path):
        self.posicao_atual += resultado
        
        if self.posicao_atual > 47:
            self.posicao_atual = 47
            
        casa = path[self.posicao_atual]
        print(f"Center       : {casa.rect.center}")
        
        if self.player_id == 1:
            self.atualiza_p1(casa)
        
        elif self.player_id == 2:
            self.atualiza_p2(casa)

        self.message()
        return self.posicao_atual 
    
    def atualiza_p1(self, casa):
        self.center = casa.rect.center
        self.player_rect = Rect(casa.x1, casa.y1, self.width, self.height)
        self.player_rect.center = casa.rect.center
        self.player_rect.center = (self.player_rect.center[0], int(self.player_rect.center[1] - 5)) 
        print(f"Player 1 Center: {self.player_rect.center}")
        
    def atualiza_p2(self, casa):
        self.center = casa.rect.center
        self.player_rect = Rect(casa.x1, casa.y1, self.width, self.height)
        self.player_rect.center = casa.rect.center
        self.player_rect.center = (self.player_rect.center[0], int(self.player_rect.center[1] + 5)) 
        print(f"Player 2 Center: {self.player_rect.center}")
        
    def message(self):
        
        if self.posicao_atual == 0:
            print("\nInício do jogo!")
        
        elif self.posicao_atual == 47:
            print(f"\nFim do jogo! Player {self.player_id} ganhou!")
        
        else:
            print("\nRole o dado novamente!")        

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.player_rect)

def main():
    
    # Network
    n = Network()
    
    # Game
    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 20
    HEIGHT = 20
    
    # This sets the margin between each cell
    MARGIN = 5

    # Y grid
    y_grid = 12

    # X grid
    x_grid = 10

    # Creating Game
    game = Game(WIDTH, HEIGHT, MARGIN, x_grid, y_grid) 
    game.create_screen(500, 255)
    game.create_board()
    game.board_coloring()
    game.create_path()

    # Player
    posicao = 0
    
    player_1 = Player('0', game.path[0], True)
    game.add_player(player_1)

    player_2 = Player('1', game.path[0], False)
    game.add_player(player_2)

    # Colors
    BACKGROUND_COLOR = (94, 191, 226) # Azul bebe

    # Loop until the user clicks the close button.
    done = False
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------

    while not done:
        
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                
                pos = pygame.mouse.get_pos()
                
                for dice in game.dice:
                    if dice.click(pos):
                        resultado = game.dice_roll()
                        p2Pos = game.read_pos(n.send(game.make_pos(player_1.center)))
                        player_2.center = p2Pos
                        posicao = player_2.atualiza_posicao(resultado, game.path)
        
        # if player_1.play:
        #     for event in pygame.event.get():  # User did something
        #         if event.type == pygame.QUIT:  # If user clicked close
        #             done = True  # Flag that we are done so we exit this loop
                
        #         elif event.type == pygame.MOUSEBUTTONDOWN:
        #             # User clicks the mouse. Get the position
                    
        #             pos = pygame.mouse.get_pos()
                    
        #             for dice in game.dice:
        #                 if dice.click(pos):
        #                     resultado = game.dice_roll()
        #                     posicao = player_1.atualiza_posicao(resultado, game.path)
        #                     player_1.play = False
        #                     player_2.play = True
        
        # elif player_2.play:
        #     for event in pygame.event.get():  # User did something
        #         if event.type == pygame.QUIT:  # If user clicked close
        #             done = True  # Flag that we are done so we exit this loop
                
        #         elif event.type == pygame.MOUSEBUTTONDOWN:
        #             # User clicks the mouse. Get the position
                    
        #             pos = pygame.mouse.get_pos()
                    
        #             for dice in game.dice:
        #                 if dice.click(pos):
        #                     resultado = game.dice_roll()
        #                     posicao = player_2.atualiza_posicao(resultado, game.path)
        #                     player_1.play = True
        #                     player_2.play = False

        # Set the screen background
        game.screen.fill(BACKGROUND_COLOR)
        
        # Draw the grid
        for row in range(x_grid):
            for column in range(y_grid):
                casa = game.grid[row][column]
                pygame.draw.rect(game.screen,
                                casa.color,
                                [casa.x1,
                                casa.y1,
                                casa.x2,
                                casa.y2])
        
        # Displaying buttons
        for dice in game.dice:
            dice.draw(game.screen)
        
        # Displaying players
        for player in game.player_list:
            player.draw(game.screen)
            if posicao == 47:
                done = True
                
        # Limit to 60 frames per second
        clock.tick(60)
                
        # Go ahead and update the screen with what we've drawn.
        pygame.display.update()
                
    # Be IDLE friendly. If you forget this line, the program will 'hang' on exit.
    time.sleep(2)
    pygame.quit()

if __name__ == "__main__":
    main()