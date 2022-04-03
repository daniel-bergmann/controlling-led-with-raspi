LED_PIN = 17

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.OUT)

#the while loop Makes the led blink every second
try:
    while True:
       #the led blinks forever if not interupted
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    #When we kill the program we are going to exit with cleanup
    GPIO.cleanup()
