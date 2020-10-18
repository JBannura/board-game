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

class Game:
    
    def __init__(self, width, height, margin, x_grid, y_grid):
        
        # Initialize pygame
        pygame.init()
        pygame.font.init()
        
        # Set title of screen
        pygame.display.set_caption("Array Backed Grid")
        
        # Criando o dado
        self.dice = [Button("Roll", 300, 77.5, (255, 255, 255))]
        
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
                self.grid[row].append(casa)  # Append a cell
    
    def add_player(self, player):
        self.player_list.append(player)
    
    def atualiza_posicao(self, posicao):
        self.actual = posicao    

    # Dice Roll
    def dice_roll(self):
        diceRoll = random.randint(1, 6)
        print(diceRoll)
        return diceRoll
    
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
        screen.blit(text, (self.button_x + round(self.button_width/2) - round(text.get_width()/2), self.button_y + round(self.button_height/2) - round(text.get_height()/2)))

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
    
    def bad_place(self):
        self.color = (222, 43, 43)
    
    def good_place(self):
        self.color = (77, 235, 87)

class Player:
    
    def __init__(self, player_id):
        
        #print(casa)
        
        self.width  = 5
        self.height = 5
        
        if player_id == '0':    
            self.color = (0, 0, 0)

        self.posicao_atual = [0, 0]
        
    def atualiza_posicao(self, resultado, screen, grid):
        
        # 10 - 10
        pos_x = self.posicao_atual[0]
        pos_y = self.posicao_atual[1]
        
        next_pos = ''
        
        self.draw()

    def draw(self, screen, casa):
        self.x = casa.x1
        self.y = casa.y1
        
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height)) 
        #font = pygame.font.SysFont('comicsans', 20)
        #text = font.render(self.button_text, 1, (0, 0, 0))
        #screen.blit(text, (self.button_x + round(self.button_width/2) - round(text.get_width()/2), self.button_y + round(self.button_height/2) - round(text.get_height()/2)))
    
# Define some colors
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (94, 191, 226) # Azul bebe
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5

# Y grid
y_grid = 10

# X grid
x_grid = 12

# Creating Game
game = Game(WIDTH, HEIGHT, MARGIN, x_grid, y_grid) 
game.create_screen(500, 255)
game.create_board()
 
# Player
player_1 = Player('0')
game.add_player(player_1)

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
                    player_1.atualiza_posicao(resultado)
 
    # Set the screen background
    game.screen.fill(BACKGROUND_COLOR)
 
    # Draw the grid
    for row in range(x_grid):
        print(row)
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
        player.draw(game.screen, game.grid[0][0])
             
    # Limit to 60 frames per second
    clock.tick(60)
             
    # Go ahead and update the screen with what we've drawn.
    pygame.display.update()
             
# Be IDLE friendly. If you forget this line, the program will 'hang' on exit.
pygame.quit()