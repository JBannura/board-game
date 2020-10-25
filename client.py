from network import Network
import random
from board import Board
from player import Player

def roll_dice(name):
    
    while True:
        choice = input(f"{name}, pressione 1 para rolar o dado: ")
        
        if choice == '1':
            roll = random.randint(10, 10)    
            print(f"{name} rolou {roll}!")
            return roll
        
        else:
            pass

def encode_to_send(roll, p1):
    p1.y = roll + p1.y
    return str(p1.x) + "," + str(p1.y) 

def decode_received(coord):
    coord = coord.split(",")
    return int(coord[1]), int(coord[2])
    
def main():
   
    n = Network()
    p = n.getP()
    p = p.split(",")
    
    player_name = input("Bem vindo ao corrida maluca!\n\nPara começar, digite seu nome: ")
    p1 = Player(player_name, p[1], p[2])
    p2 = Player('', 1, 0)
    board = Board(p1, p2)
    board.refresh()
    
    if int(p[0]) == 0:
        play = True
    else:
        play = False
    
    run = True
    
    while run:   
        
        # if play == False:
        #     print("Aguarde a vez do outro jogador.")
        
        # while play != True:
        #     try:
        #         n.send('False')
        #         play = bool(n.receive().split(",")[-1])
            
        #     except:
        #         pass
            
        #     print(f"Play: {play}")
            
        n.send(encode_to_send(roll_dice(player_name), p1))
        p2_status = decode_received(n.receive())

        p2.x = p2_status[0]
        p2.y = p2_status[1]
        
        board.refresh()

        if p1.win:
            print(f"Parabéns {p1.name} você venceu!!")
            print("\nFim de jogo.")
            
        
        elif p2.win:
            print(f"Que pena {p2.name}, você perdeu...")
            print("\nFim de jogo.")
            break
            
main()

        