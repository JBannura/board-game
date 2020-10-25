import socket
import select
from _thread import *
import time
import sys

server = "localhost"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

player_status = ['1,0', '2,0']

# Servidor esta esperando 2 clientes se conectarem
s.listen(2)
print("Server iniciado! Esperando jogadores...")
 
def threaded_client(conn, jogador):
    
    if jogador == 0:
        conn.send(str.encode("0,1,0"))
    elif jogador == 1:
        conn.send(str.encode("1,2,0"))
        
    reply = ""
    while True:
        
        try:
            conn.settimeout(1)
            data = conn.recv(2048*8)
            conn.settimeout(None)
            print(f"Data: {data}")
            
            data_aux = data.decode("utf-8")
            
            if data_aux == 'False':
                flag = False
            
            else:
                player_status[jogador] = data_aux
                flag = True
                
            if not data:
                print("Desconectado!")
                break
            
            else:
                if jogador == 0:
                    reply = f'Player 2,{player_status[1]},{flag}'
                else:
                    reply = f'Player 1,{player_status[0]},{flag}'
                
                print("Recebido: ", data)
                print("Enviando: ", reply)

            conn.sendall(str.encode(reply))
        
        except socket.timeout as e:
                
                err = e.args[0]
                if err == 'timed out':
                    #print("Recv timed out... trying again!")
                    pass
                
                else:
                    print(f"Real error: {err}")    
            
        except:
            break
        
        #breakpoint()

    print("Conexão perdida!")
    conn.close()
    
currentPlayer = 0

while True:
    conn, addr = s.accept()
    
    print("Conectado com: ", addr)

    status = start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1