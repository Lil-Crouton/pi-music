import socket

def initialize_client():
	HEADER = 16
	PORT = 5050
	FORMAT = 'utf-8'
	DISCONNECT_MESSAGE = '!DISCONNECT'
	SERVER = '192.168.0.30'
	ADDR = (SERVER,PORT)
	config = {'HEADER':HEADER,
		  'PORT':PORT,
		  'FORMAT':FORMAT,
		  'DISCONNECT_MESSAGE':DISCONNECT_MESSAGE,
		  'SERVER':SERVER,
		  'ADDR':(SERVER,PORT)}

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(ADDR)

	return(config,client)

def send(msg,config,client):
	# Need to encode msg in format compatible with the server
	message = msg.encode(config['FORMAT'])
	# First msg sent needs to be length of header
	# Need to pad the msg to make it length of 64
	msg_length = len(message)
	send_length = str(msg_length).encode(config['FORMAT'])
	# Substract msg length from header, convert it to byte format, then add to send_length
	send_length += b' ' * (config['HEADER'] - len(send_length))
	client.send(send_length)
	client.send(message)
	print(client.recv(config['HEADER']).decode(config['FORMAT']))

if __name__ == '__main__':
	(config,client) = initialize_client()
	send("hello world",config,client)
	send("What up",config,client)
	send("!DISCONNECT",config,client)
