
import math
import time
import RPi.GPIO as GPIO
import pantilthat

delay = 0.05 

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
GPIO.setup(18, GPIO.OUT)  # set up pin 18
GPIO.output(18, 1)  # turn on pin 18
GPIO.setwarnings(False)

foo = 0
for z in range(0, 2160):
    x = 10 * math.cos(foo)
    y = 10 * math.sin(foo)
    pantilthat.pan(x)
    pantilthat.tilt(y)
    print(foo, x, y)
    time.sleep(delay)
    foo += 0.003

foo = 0
for z in range(0, 360):
    x = 10 * math.cos(math.radians(z))
    y = 10 * math.sin(math.radians(z))
    pantilthat.pan(x)
    pantilthat.tilt(y)
    print(z, x, y)
    time.sleep(delay)
    