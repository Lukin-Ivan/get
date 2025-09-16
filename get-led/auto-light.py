import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
phototransistor = 6
GPIO.setup(phototransistor, GPIO.IN)
while True:
    GPIO.output(led, not GPIO.input(phototransistor))