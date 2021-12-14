import time
import board
import neopixel

class Lights:
    def __init__(self,PIN,NUM_LIGHTS):
        self.pixels = neopixel.NeoPixel(PIN,NUM_LIGHTS)
        self.color = (255,215,0)

    def fadeOn(self):
        self.pixels.brightness = 0
        self.pixels.fill(self.color)

        i = 0
        fadeTime = 2 #s
        for i in range(0,10000):
            self.pixels.brightness = round((i**3)/(10000**3),2)
            #time.sleep(fadeTime/100)
        print('success')

if __name__ == '__main__':
    lights = Lights(board.D18,300)
    lights.fadeOn()

