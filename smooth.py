"""My Cat Laser Pythong"""
#!/usr/bin/python3

import math
import time
import RPi.GPIO as GPIO
import pantilthat

#Zero is the bottom
DELAY = 0.05
TILT = 10
PANLEFT = 75
PANRIGHT = -10



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

def drawline(panright=0, panleft=0, step=0):
    """Draws a line panning right left, left right"""
    #print("Draw Lines")
    pantilthat.tilt(TILT)
    for pan_deg in range(panright, panleft, step):
        pantilthat.pan(pan_deg)
        time.sleep(0.10)
        print("Line TILT=%d, PAN=%d" % (TILT, pan_deg))
    return

def drawcircle(offset=0, start=0, stop=360, step=2):
    """Draw a circle from cos / sin """
    #print("Draw Circle", offset)
    for servo_deg in range(start, stop, step):
        x_cart = offset+(8 * math.cos(math.radians(servo_deg)))
        y_cart = 8 * math.sin(math.radians(servo_deg))
        pantilthat.pan(x_cart)
        pantilthat.tilt(y_cart + TILT)
        #print(z, x, y)
        time.sleep(DELAY)
        print("Circle TILT=%d, PAN=%d" % (y_cart, x_cart))
    return

def main():
    """ Main """
    setup()
    for laser_laps in range(1, 20):
        drawcircle(PANRIGHT, 0, 360, 2)
        # Draw line up steps PANRIGHT to PANLEFT going positive facing out
        drawline(PANRIGHT, PANLEFT, 1)
        drawcircle(PANLEFT, 180, 360, 2)
        drawcircle(PANLEFT, 360, 180, -2)
        # Draw line down steps PANLEFT to PANRIGHT going negitive facing out
        drawline(PANLEFT, PANRIGHT, -1)
    shutdown()
    return

if __name__ == "__main__":
    main()
