import socket
from _thread import *
import sys

server = "192.168.15.36"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# Servidor esta esperando 2 clientes se conectarem
s.listen(2)
print("Server iniciado! Esperando jogadores...")

def threaded_client(conn):
    conn.send(str.encode("Conectado!"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Desconectado!")
                break
            else:
                print("Recebido: ", reply)
                print("Enviando: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Conexão perdida!")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Conectado com:", addr)

    start_new_thread(threaded_client, (conn,))