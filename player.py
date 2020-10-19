import pygame
from pygame import Rect

class Player:
    
    def __init__(self, player_id, play):
        
        self.width  = 3
        self.height = 3
        self.play   = play
        
        if player_id == '0':    
            self.color = (0, 0, 0)
            self.player_id = 1
            
            self.player_rect = Rect(30, 30, self.width, self.height)
            self.player_rect.center = (40, 35)
            self.center = (40, 35)
            
        elif player_id == '1':
            
            self.color = (188, 51, 215)
            self.player_id = 2
                
            self.player_rect = Rect(30, 30, self.width, self.height)
            self.player_rect.center = (40, 45)
            self.center = (40, 45)  
        
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
        #print(f"Player 1 Center: {self.player_rect.center}")
        
    def atualiza_p2(self, casa):
        self.center = casa.rect.center
        self.player_rect = Rect(casa.x1, casa.y1, self.width, self.height)
        self.player_rect.center = casa.rect.center
        self.player_rect.center = (self.player_rect.center[0], int(self.player_rect.center[1] + 5)) 
        #print(f"Player 2 Center: {self.player_rect.center}")
        
    def message(self):
        
        if self.posicao_atual == 0:
            print("\nInício do jogo!")
        
        elif self.posicao_atual == 47:
            print(f"\nFim do jogo! Player {self.player_id} ganhou!")
        
        else:
            print("\nRole o dado novamente!")        

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.player_rect)