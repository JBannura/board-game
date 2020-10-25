import pygame
from network import Network

width = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

def atualizaJanela(win, jogador, jogador2):
    win.fill((255, 255, 255))
    jogador.desenha(win)
    jogador2.desenha(win)
    pygame.display.update()
    
def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()
    
    while run:

        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        p.movimentacao()
        atualizaJanela(win, p, p2)   

main()