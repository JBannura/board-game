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

# Initialize pygame
pygame.init()
pygame.font.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [500, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")

class Button:
    
    # Button creation
    
    def __init__(self, text, x, y, color):
        
        self.button_text   = text 
        self.button_x      = x
        self.button_y      = y
        self.button_color  = color
        self.button_width  = 50
        self.button_height = 35

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
    
    # Dice Roll
    def dice_roll(self):
        diceRoll = random.randint(1, 6)
        return diceRoll

btns = [Button("Roll", 300, 77.5, (255, 255, 255))]

# Define some colors
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (94, 191, 226)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5

# Y grids
# X grids

y_grid = 10
x_grid = 10
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(x_grid):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(y_grid):
        grid[row].append(0)  # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[0][0] = 1
 
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
            
            for btn in btns:
                if btn.click(pos):
                    print(btn.dice_roll())
            
            # # Change the x/y screen coordinates to grid coordinates
            # column = pos[0] // (WIDTH + MARGIN)
            # row = pos[1] // (HEIGHT + MARGIN)
            
            # # Set that location to one
            # grid[row][column] = 1
            # print("Click ", pos, "Grid coordinates: ", row, column)
 
    # Set the screen background
    screen.fill(BACKGROUND_COLOR)
 
    # Draw the grid
    for row in range(x_grid):
        for column in range(y_grid):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    
    # Displaying buttons
    for btn in btns:
        btn.draw(screen)
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.update()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()