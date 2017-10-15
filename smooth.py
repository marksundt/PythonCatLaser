#!/usr/bin/env python

import math
import time
import RPi.GPIO as GPIO
import pantilthat

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom

GPIO.setup(17, GPIO.OUT)  # set up pin 17
GPIO.setup(18, GPIO.OUT)  # set up pin 18

GPIO.output(17, 1)  # turn on pin 17
GPIO.output(18, 1)  # turn on pin 18

pantilthat.tilt(-70) 

while True:
    # Get the time in seconds
    t = time.time()

    # G enerate an angle using a sine wave (-1 to 1) multiplied by 90 (-90 to 90)
    a = math.sin(t * 2) * 45
    
    # Cast a to int for v0.0.2
    a = int(a)

    pantilthat.pan(a)


    # Two decimal places is quite enough!
    print(round(a,2))

    # Sleep for a bit so we're not hammering the HAT with updates
    time.sleep(0.5)
