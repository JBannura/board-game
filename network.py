import socket
import select

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()
        
    def getP(self):
        return self.p
        
    # Conectar
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048*8).decode()
        except:
            pass

    # Enviar
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            
        except socket.error as e:
            print(e)
    
    def receive(self):
        
        try:    
            try:
                self.client.settimeout(1)
                data = self.client.recv(2048*8)
                self.client.settimeout(None)
                return data.decode("utf-8")
            
            except socket.timeout as e:        
                err = e.args[0]
                if err == 'timed out':
                    print("Recv timed out... trying again!")
                else:
                    print(f"Real error: {err}")

        except Exception as e:
            print(f"Receive Excpetion: {e}")