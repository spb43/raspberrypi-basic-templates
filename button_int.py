import RPi.GPIO as GPIO
import time

buttonPin = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttonHandler(channel):
    print("in_buttonHandler...")
GPIO.add_event_detect(buttonPin, GPIO.RISING, callback=buttonHandler, bouncetime=300)

try:
    while(True):
        time.sleep(0.1);

except KeyboardInterrupt:
    GPIO.cleanup();
    print("Quit")

