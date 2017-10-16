"""My Cat Laser Pythong"""
#!/usr/bin/python3

import math
import time
import RPi.GPIO as GPIO
import pantilthat

Delay = 0.05

def setup():
    """Setup for GPIO and LED fuctions"""
    print("Setup")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
    GPIO.setup(18, GPIO.OUT)  # set up pin 18
    GPIO.output(18, 1)  # turn on pin 18
    return

def shutdown():
    """Clean up GPIO"""
    GPIO.output(18, 1)  # turn off pin 18 laser
    GPIO.cleanup()
    return

def drawlinesup():
    """Draws a line on tilt from 60 to -60 up steps"""
    print("Draw Lines Up")
    pantilthat.tilt(0)
    x = 60
    # 60 to zero
    for y in range(0, 60):
        pantilthat.pan(x)
        time.sleep(Delay)
        x -= 1
    # zero to -60
    for y in range(0, 20):
        pantilthat.pan(x)
        time.sleep(Delay)
        x -= 1
    return

def drawlinesdown():
    """Draws a line on tilt from -60 to 60 down steps"""
    print("Draw Lines Down")
    pantilthat.tilt(0)
    x = -20
    # -60 to zero
    for y in range(0, 20):
        pantilthat.pan(x)
        time.sleep(Delay)
        x += 1
    # zero to 60
    for y in range(0, 60):
        pantilthat.pan(x)
        time.sleep(Delay)
        x += 1
    return

def drawcircle(offset=0):
    """Draw a circle from cos / sin - need offset"""
    print("Draw Circle", offset)
    for z in range(0, 360):
        x = offset+(8 * math.cos(math.radians(z)))
        y = 8 * math.sin(math.radians(z))
        pantilthat.pan(x)
        pantilthat.tilt(y)
        #print(z, x, y)
        time.sleep(Delay)
    return

def main():
    """ Main """
    setup()

    for i in range(1, 20):
        drawcircle(60)
        drawlinesup()
        drawcircle(-20)
        drawlinesdown()
    shutdown()
    return

if __name__ == "__main__":
    main()
