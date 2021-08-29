import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 300, auto_write=False)
pixels.show()
