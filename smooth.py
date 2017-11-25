"""My Cat Laser Pythong"""
#!/usr/bin/python3
import sys
import math
import time
import RPi.GPIO as GPIO
import pantilthat


#Zero is the bottom
DELAY = 0.05
TILT = 10
PANLEFT = 75
PANRIGHT = -10
# Start / Stop line to join circle
PANOFFSET = 7

def setup():
    """Setup for GPIO and LED fuctions"""
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
    """Draws a line panning right left, left right offset starts line at circle"""
    pantilthat.tilt(TILT)
    for pan_deg in range(panright, panleft, step):
        pantilthat.pan(pan_deg)
        time.sleep(0.10)
        #print("Line TILT=%d, PAN=%d" % (TILT, pan_deg))
    return

def drawcircle(panoffset=0, start=0, stop=360, step=2):
    """Draw a circle from cos / sin """
    for servo_deg in range(start, stop, step):
        x_cart = panoffset+(8 * math.cos(math.radians(servo_deg)))
        y_cart = 8 * math.sin(math.radians(servo_deg))
        pantilthat.pan(x_cart)
        pantilthat.tilt(y_cart + TILT)
        time.sleep(DELAY)
        #print("Circle TILT=%d, PAN=%d" % (y_cart + TILT, x_cart))
    return

def main():
    """ Main """
    if len(sys.argv) > 1:
        laser_laps = int(sys.argv[1])
        print("Laser Laps = %d" % (laser_laps))
    else:
        laser_laps = 20

    setup()
    for x in range(laser_laps):
        drawcircle(PANRIGHT, 0, 360, 2)
        # Draw line up steps PANRIGHT to PANLEFT going positive facing out
        drawline(PANRIGHT + PANOFFSET, PANLEFT - PANOFFSET, 1)
        drawcircle(PANLEFT, 180, 360, 2)
        drawcircle(PANLEFT, 360, 180, -2)
        # Draw line down steps PANLEFT to PANRIGHT going negitive facing out
        drawline(PANLEFT - PANOFFSET, PANRIGHT + PANOFFSET, -1)
    shutdown()
    return

if __name__ == "__main__":
    main()
