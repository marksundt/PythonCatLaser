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

for x in range(-60, 60)

    pantilthat.pan(x)


    # Two decimal places is quite enough!
    print(x)

    # Sleep for a bit so we're not hammering the HAT with updates
    time.sleep(0.05)
