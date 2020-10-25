def str_encode():
    
    teste = 'Player 1,0'
    
    splittado = teste.split(',')
    
    jogador = splittado[0]
    posicao = splittado[1]
    
    print(f"{jogador} na posicao: {posicao}")
    
str_encode()