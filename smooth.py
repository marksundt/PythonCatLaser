#!/usr/bin/env python

import math
import time
import RPi.GPIO as GPIO
import pantilthat

delay = 0.05 

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom

GPIO.setup(17, GPIO.OUT)  # set up pin 17
GPIO.setup(18, GPIO.OUT)  # set up pin 18

GPIO.output(17, 1)  # turn on pin 17
GPIO.output(18, 1)  # turn on pin 18

pantilthat.tilt(-70) 


while True:
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