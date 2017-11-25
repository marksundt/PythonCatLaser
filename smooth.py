"""My Cat Laser Pythong"""
#!/usr/bin/python3

import math
import time
import RPi.GPIO as GPIO
import pantilthat

DELAY = 0.05
TOP = 65
BOTTOM = -20
TILT = 10

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
    GPIO.output(18, 0)  # turn off pin 18 laser
    GPIO.cleanup()
    return

def drawlinesup():
    """Draws a line on tilt from 80 to -20 up steps"""
    print("Draw Lines Up")
    pantilthat.tilt(TILT)
    pan_deg = TOP
    # zero to top where circle should start
    # I hate that I couldnt do list(range(0,-20))
    for pan_steps in range(0, TOP):
        pantilthat.pan(pan_deg)
        time.sleep(DELAY)
        pan_deg -= 1
    # zero to -20
    for pan_steps in range(0, 20):
        pantilthat.pan(pan_deg)
        time.sleep(DELAY)
        pan_deg -= 1
    return

def drawlinesdown():
    """Draws a line on tilt from -60 to 60 down steps"""
    print("Draw Lines Down")
    pantilthat.tilt(TILT)
    pan_deg = -20
    # -60 to zero
        # I hate that I couldnt do list(range(-20,0)) - No step function
    for pan_steps in range(0, 20):
        pantilthat.pan(pan_deg)
        time.sleep(DELAY)
        pan_deg += 1
    # zero to 80
    for pan_steps in range(0, TOP):
        pantilthat.pan(pan_deg)
        time.sleep(DELAY)
        pan_deg += 1
    return

def drawcircle(offset=0):
    """Draw a circle from cos / sin - need offset"""
    print("Draw Circle", offset)
    for servo_steps in range(0, 360):
        x_cart = offset+(8 * math.cos(math.radians(servo_steps)))
        y_cart = 8 * math.sin(math.radians(servo_steps))
        pantilthat.pan(x_cart)
        pantilthat.tilt(y_cart)
        #print(z, x, y)
        time.sleep(DELAY)
    return

def main():
    """ Main """
    setup()

    for laser_laps in range(1, 20):
        drawcircle(TOP)
        drawlinesup()
        drawcircle(BOTTOM)
        drawlinesdown()
    shutdown()
    return

if __name__ == "__main__":
    main()
