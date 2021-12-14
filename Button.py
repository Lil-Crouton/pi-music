import RPi.GPIO as GPIO
import time
import main

class Button:
    def __init__(self,button_id,wait_time):
        self.BUTTON = button_id
        self.WAIT = wait_time
        self.press = False

    def detect_rising(self,state,i):
        temp = state.copy()
        temp[i] = 0
        if (temp == 10*[0]) and (state[i] == 1):
            press = True
        else:
            press = False

        return(press)

    def button_listen(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.BUTTON,GPIO.IN,pull_up_down=GPIO.PUD_UP)
        state = 10*[1]
        i = 0
        db_timer = 10
        while True:
            state[i] = GPIO.input(self.BUTTON)
            #print(state[i])
            self.press = self.detect_rising(state,i)
            if self.press:
                return True
            #if press and (time.time()-db_timer > self.WAIT):
            #    main.start_music()
            #    db_timer = time.time()


            if i < 9:
                i += 1
            else:
                i = 0
            time.sleep(0.01)


if __name__ == '__main__':
    button = Button(3,5)
    print(button.button_listen())
    GPIO.cleanup()
