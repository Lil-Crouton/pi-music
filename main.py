from Client import *
from Button import *
from Lights import *
import threading
import time
import board
import RPi.GPIO as GPIO

if __name__ == '__main__':
    BUTTON_GPIO = 3
    BUTTON_WAIT_TIME = 5 #s
    LIGHT_PIN = board.D18
    NUM_LIGHTS = 300
    CLIENT_CONFIG = {'HEADER':16,
                     'PORT':5050,
                     'FORMAT':'utf-8',
                     'DISCONNECT_MESSAGE':'!DISCONNECT',
                     'SERVER':'192.168.0.30',
                     'ADDR':('192.168.0.30',5050)}
    
    button = Button(BUTTON_GPIO, BUTTON_WAIT_TIME)
    print('Initializing Client')
    client = Client(CLIENT_CONFIG)
    lights = Lights(LIGHT_PIN,NUM_LIGHTS)

    while True: 
        if button.button_listen():
        #    print('Fading On')
        #   thread = threading.Thread(target=lights.fadeOn)
        #    thread.start()
            client = Client(CLIENT_CONFIG)
            print('Sending [ALBUM] After Hours')
            client.send('[ALBUM] After Hours')
            client.send('!DISCONNECT')

    GPIO.cleanup()
