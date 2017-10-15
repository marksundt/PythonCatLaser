#!/usr/bin/python3

import math
import time
import RPi.GPIO as GPIO
import pantilthat

delay = 0.05

def setup():
    print("Setup")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
    GPIO.setup(18, GPIO.OUT)  # set up pin 18
    GPIO.output(18, 1)  # turn on pin 18
    return

def shutdown():
    GPIO.output(18, 1)  # turn off pin 18 laser
    GPIO.cleanup()
    return

def drawlines():
    print("Draw Lines")
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
    print("Draw Circle")
    for z in range(0, 360):
        x = 10 * math.cos(math.radians(z))
        y = 10 * math.sin(math.radians(z))
        pantilthat.pan(x)
        pantilthat.tilt(y)
        #print(z, x, y)
        time.sleep(delay)   
    return

def main():
    setup()

    for i in range(1, 20):
        drawcircle()
        drawlines()
    
    shutdown()
    return

if __name__ == "__main__":
    main()