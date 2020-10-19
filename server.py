import socket
from _thread import *
import sys
import pickle
#from player import Player
from tim_player import Player 

server = "192.168.0.17"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# Servidor esta esperando 2 clientes se conectarem
s.listen(2)
print("Server iniciado! Esperando jogadores...")

players = [Player(0, 0, 50, 50, (255, 0, 0)), Player(100, 100, 50, 50, (0, 0, 255))]
 
def threaded_client(conn, jogador):
    conn.send(pickle.dumps(players[jogador]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[jogador] = data

            if not data:
                print("Desconectado!")
                break
            else:
                if jogador == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Recebido: ", data)
                print("Enviando: ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Conexão perdida!")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Conectado com: ", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1