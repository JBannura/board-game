import pygame

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