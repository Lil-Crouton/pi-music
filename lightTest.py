import time
import board
import neopixel

def fadeOn():
	pixels = neopixel.NeoPixel(board.D18,300)

	pixels.brightness = 0
	pixels.fill((255,0,0))

	i = 0
	fadeTime = 2 #s
	for i in range(0,10000):
		pixels.brightness = round((i**3)/(10000**3),2)
		#time.sleep(fadeTime/100)

