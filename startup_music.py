from Client import *
import json

with open('/home/pi/pi-music/client_config.json','r') as config_file:
    config_data = config_file.read()
        
CLIENT_CONFIG = json.loads(config_data)
CLIENT_CONFIG['ADDR'] = (CLIENT_CONFIG['SERVER'],CLIENT_CONFIG['PORT'])


client = Client(CLIENT_CONFIG)

client.send('[ALBUM] After Hours')
client.send('!DISCONNECT')

