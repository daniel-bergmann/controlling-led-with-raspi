LED_PIN = 17

#importing the library as GPIO to make the code more clean
import RPi.GPIO as GPIO
import time

#sleccting the GPIO by the number
GPIO.setmode(GPIO.BCM)

#connecting to led to output mode
GPIO.setup(LED_PIN, GPIO.OUT)

#turning the led on with GPIO.HIGH
GPIO.output(LED_PIN, GPIO.HIGH)
#putting the program to leep after 5 seconds
time.sleep(5)

#best practice just before the program exits in order to get the program out of output mode before running othe programs. Otherwise I could damage the raspi GPIO
GPIO.cleanup()
