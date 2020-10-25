# Game
import pygame
import board 
import player

# Connection
import network

# Utils
import time

def atualiza_janela(game, player_1, player_2):
    player_1.draw(game.screen)
    player_2.draw(game.screen)
    pygame.display.update()
    
def main():
    
    # Network
    n = network.Network()
    
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

    # Colors
    BACKGROUND_COLOR = (94, 191, 226) # Azul bebe
    
    # Creating Game
    game = board.Game(WIDTH, HEIGHT, MARGIN, x_grid, y_grid) 
    game.create_screen(500, 255)
    game.create_board()
    game.board_coloring()
    game.create_path()
    game.screen.fill(BACKGROUND_COLOR)

    # Player
    posicao = 0
    
    player_1 = player.Player('0', True)
    game.add_player(player_1)

    player_2 = player.Player('1', False)
    game.add_player(player_2)

    # Loop until the user clicks the close button.
    done = False
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
    while not done:
        
        clock.tick(60)
        
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         done = True
        #         pygame.quit()
        
        #     elif event.type == pygame.MOUSEBUTTONDOWN:
        #         pos = pygame.mouse.get_pos()
                
        #         for dice in game.dice:
        #             if dice.click(pos):
        #                 resultado = game.dice_roll()
        #                 posicao = player_1.atualiza_posicao(resultado, game.path)
            
        #             # Set the screen background
        #     game.screen.fill(BACKGROUND_COLOR)
            
        #     # Draw the grid
        #     for row in range(x_grid):
        #         for column in range(y_grid):
        #             casa = game.grid[row][column]
        #             pygame.draw.rect(game.screen,
        #                             casa.color,
        #                             [casa.x1,
        #                             casa.y1,
        #                             casa.x2,
        #                             casa.y2])
            
        #     # Displaying buttons
        #     for dice in game.dice:
        #         dice.draw(game.screen)
            
        #     # Displaying players
        #     for player_ in game.player_list:
        #         player_.draw(game.screen)
        #         if posicao == 47:
        #             done = True
            
        #     atualiza_janela(game, player_1, player_2)
                          
        if player_1.play:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    
                    for dice in game.dice:
                        if dice.click(pos):
                            resultado = game.dice_roll()
                            posicao = player_1.atualiza_posicao(resultado, game.path)
                            player_1.play = False
                            player_2.play = True
        
        elif player_2.play:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    
                    for dice in game.dice:
                        if dice.click(pos):
                            resultado = game.dice_roll()
                            posicao = player_2.atualiza_posicao(resultado, game.path)
                            player_1.play = True
                            player_2.play = False
                        
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
        for player_ in game.player_list:
            player_.draw(game.screen)
            if posicao == 47:
                done = True
        
        # Update screen
        pygame.display.update()
                
    # Be IDLE friendly. If you forget this line, the program will 'hang' on exit.
    time.sleep(2)
    pygame.quit()

if __name__ == "__main__":
    main()