from client import *
#import lightTest as lights
import threading
import time

def start_music():
	print('Fading On')
	#thread = threading.Thread(target=lights.fadeOn)
	#thread.start()

	print('Initializing Client')
	(config,client) = initialize_client()
	print('Sending [ALBUM] After Hours')
	send('[ALBUM] After Hours',config,client)
	send('!DISCONNECT',config,client)

