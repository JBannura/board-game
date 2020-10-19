import socket
from _thread import *
import sys

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

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(0,0),(100,100)]
 
def threaded_client(conn, jogador):
    conn.send(str.encode(make_pos(pos[jogador])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048 * 8).decode())
            pos[jogador] = data

            if not data:
                print("Desconectado!")
                break
            else:
                if jogador == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Recebido: ", data)
                print("Enviando: ", reply)

            conn.sendall(str.encode(make_pos(reply)))
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