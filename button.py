import RPi.GPIO as GPIO
import time
import main

def detect_rising(state,i):
	# Check for state change
	if state[i] == 0 and state[i-1] == 1:
		change = True
	else:
		change = False

	# Detect falling edge and valid duration of press
	temp = state.copy()
	temp[i] = 0
	if (temp == 10*[0]) and (state[i] == 1):
		press = True
	else:
		press = False

	return(press)

def button_listen(BUTTON):
	GPIO.setwarnings(False)
	#GPIO.setmode(GPIO.BOARD)
	GPIO.setup(BUTTON,GPIO.IN,pull_up_down=GPIO.PUD_UP)
	state = 10*[1]
	i = 0
	db_timer = 10
	while True:
		state[i] = GPIO.input(BUTTON)
		press = detect_rising(state,i)

		if press and (time.time()-db_timer > 5):
			main.start_music()
			db_timer = time.time()


		if i < 9:
			i += 1
		else:
			i = 0
		time.sleep(0.01)


if __name__ == '__main__':
	BUTTON = 12
	button_listen(BUTTON)
	GPIO.cleanup()
