#!/usr/bin/python3

import math
import time
import RPi.GPIO as GPIO
import pantilthat

def setup():

    delay = 0.05 

    GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
    GPIO.setup(18, GPIO.OUT)  # set up pin 18
    GPIO.output(18, 1)  # turn on pin 18
    GPIO.setwarnings(False)

def drawlines():
    pantilthat.tilt(0) 
    x = 60
    # 60 to zero
    for y in range(0, 60):
        pantilthat.pan(x)
        time.sleep(delay)
        x -= 1
    # zero to -60
    for y in range(0, 60):
        pantilthat.pan(x)
        time.sleep(delay)
        x -= 1
    # -60 to zero
    for y in range(0, 60):
        pantilthat.pan(x)
        time.sleep(delay)
        x += 1
    # zero to 60
    for y in range(0, 60):
        pantilthat.pan(x)
        time.sleep(delay)
        x += 1
    return

def drawcircle():
    for z in range(0, 360):
        x = 10 * math.cos(math.radians(z))
        y = 10 * math.sin(math.radians(z))
        pantilthat.pan(x)
        pantilthat.tilt(y)
        #print(z, x, y)
        time.sleep(delay)   
        return

if __name__ == "__main__":
    main()
        setup()
        drawcircle()
        drawlines()
        drawcircle()
