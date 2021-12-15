from Client import *
from Button import *
from Lights import *
import threading
import time
import board
import RPi.GPIO as GPIO
import json

def main():
    # Configuration Data
    BUTTON_GPIO = 3
    BUTTON_WAIT_TIME = 5 #s
    LIGHT_PIN = board.D18
    NUM_LIGHTS = 300
    
    with open('/home/pi/pi-music/client_config.json','r') as config_file:
        config_data = config_file.read()

    CLIENT_CONFIG = json.loads(config_data)
    CLIENT_CONFIG['ADDR'] = (CLIENT_CONFIG['SERVER'],CLIENT_CONFIG['PORT'])
    
    # Class Initialization
    button = Button(BUTTON_GPIO, BUTTON_WAIT_TIME)
    print('Initializing Client')
    client = Client(CLIENT_CONFIG)
    lights = Lights(LIGHT_PIN,NUM_LIGHTS)
    
    # Main Loop
    while True: 
        if button.button_listen():
        #    print('Fading On')
        #   thread = threading.Thread(target=lights.fadeOn)
        #    thread.start()
            client = Client(CLIENT_CONFIG)
            print('Sending [ALBUM] After Hours')
            client.send('[ALBUM] After Hours')
            client.send('!DISCONNECT')
    
    # Cleanup
    GPIO.cleanup()

if __name__ == '__main__':
   main() 
