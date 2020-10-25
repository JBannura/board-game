import pygame

class Player():
    
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.pos = (x, y, width, height)
        self.vel = 3
        
        
    def desenha(self, win):
        pygame.draw.rect(win, self.color, self.pos)
    
    def movimentacao(self):
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        
        if keys[pygame.K_UP]:
            self.y -= self.vel
        
        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()
            
    def update(self):
        self.pos = (self.x, self.y, self.width, self.height)