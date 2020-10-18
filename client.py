import pygame
from network import Network

width = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

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
            
        self.pos = (self.x, self.y, self.width, self.height)
        
def atualizaJanela(win, jogador):
     
    win.fill((255, 255, 255))
    jogador.desenha(win)
    pygame.display.update()
    
def main():
    run = True
    n = Network()
    startPos = n.getPos()
    p = Player(50, 50, 100, 100, (0, 255, 0))
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        p.movimentacao()
        atualizaJanela(win, p)   

main()