import socket

class Client:
    def __init__(self,CONFIG):
        self.config = CONFIG
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.config['ADDR'])

    def send(self,msg):
        # Need to encode msg in format compatible with the server
        message = msg.encode(self.config['FORMAT'])
        # First msg sent needs to be length of header
        # Need to pad the msg to make it length of 64
        msg_length = len(message)
        send_length = str(msg_length).encode(self.config['FORMAT'])
        # Substract msg length from header, convert it to byte format, then add to send_length
        send_length += b' ' * (self.config['HEADER'] - len(send_length))
        self.client.send(send_length)
        self.client.send(message)
        print(self.client.recv(self.config['HEADER']).decode(self.config['FORMAT']))

if __name__ == '__main__':
    HEADER = 16
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = '!DISCONNECT'
    SERVER = '192.168.0.30'
    ADDR = (SERVER,PORT)
    CLIENT_CONFIG = {'HEADER':HEADER,
                     'PORT':PORT,
                     'FORMAT':FORMAT,
                     'DISCONNECT_MESSAGE':DISCONNECT_MESSAGE,
                     'SERVER':SERVER,
                     'ADDR':(SERVER,PORT)}
    client_object = Client(CLIENT_CONFIG)
    client_object.send("hello world")
    client_object.send("What up")
    client_object.send("!DISCONNECT")
