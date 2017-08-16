#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

# global GPIO constants
RED_LIGHT = 16
YELLOW_LIGHT = 20
GREEN_LIGHT = 21
RUNNING = True

# Time intervals constants
RED_DURATION = 6
YELLOW_DURATION = 2
GREEN_DURATION = 5

# a function that update states 
def updateState(green, yellow, red):
    GPIO.output(RED_LIGHT, red)
    GPIO.output(YELLOW_LIGHT, yellow)
    GPIO.output(GREEN_LIGHT, green)


GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LIGHT, GPIO.OUT)
GPIO.setup(YELLOW_LIGHT, GPIO.OUT)
GPIO.setup(GREEN_LIGHT, GPIO.OUT)
 
print "Traffic Light started. Press CTRL + C to quit"
 

try:
    while RUNNING:
        # GPIO.LOW = 0, GPIO.HIGH = 1
        # GREEN ON, YELLOW OFF, RED OFF
        updateState(GPIO.HIGH, GPIO.LOW, GPIO.LOW)
        time.sleep(RED_DURATION)
        # GREEN OFF, YELLOW ON, RED OFF
        updateState(GPIO.LOW, GPIO.HIGH, GPIO.LOW)
        time.sleep(YELLOW_DURATION)
        # GREEN OFF, YELLOW OFF, RED ON
        updateState(GPIO.LOW, GPIO.LOW, GPIO.HIGH)
        time.sleep(GREEN_DURATION)

except KeyboardInterrupt:
    RUNNING = False
    print "\Stopping"

finally:
    print "\Cleaning up GPIOs"
    GPIO.cleanup()
