import board
import neopixel

#def lights_off():
pixels = neopixel.NeoPixel(board.D18, 300, auto_write=False)
pixels.show()

#if __name__ == 'main':
#	lights_off()
