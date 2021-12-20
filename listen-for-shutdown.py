#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import subprocess
import board
import neopixel


def listenForEdge():
	GPIO.wait_for_edge(3, GPIO.FALLING)
	timer = time.time()
	while not GPIO.input(3):
		if time.time()-timer > 3:
			return True
	return False

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
shutdown = listenForEdge()

while not shutdown:
	shutdown = listenForEdge()

print('SHUTDOWN')
pixels = neopixel.NeoPixel(board.D18, 300, auto_write=False)
pixels.show()
subprocess.call(['shutdown', '-h', 'now'], shell=False)
