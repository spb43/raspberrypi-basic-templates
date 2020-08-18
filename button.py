import RPi.GPIO as GPIO
import time

buttonPin = 5

GPIO.setmode(GPIO.BCM)

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23

try:
    while True:
        button_state = GPIO.input(buttonPin)
        if button_state == False:
            print('Button Pressed...')
            time.sleep(0.2)
        else:
            time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print "Quit"
