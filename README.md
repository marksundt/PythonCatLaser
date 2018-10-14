# PythonCatLaser

crontab -e (for admin jobs)


* * * * * *
| | | | | | 
| | | | | +-- Year              (range: 1900-3000)
| | | | +---- Day of the Week   (range: 1-7, 1 standing for Monday)
| | | +------ Month of the Year (range: 1-12)
| | +-------- Day of the Month  (range: 1-31)
| +---------- Hour              (range: 0-23)
+------------ Minute            (range: 0-59)

*/15 9-17 * * 1-5  (Every 15 min, 9am to 5pm, Mon-Fri)
************* This is what I have on the CAT Laser **********
 */15 21-22 * * *   /usr/bin/python3 /home/pi/python/pantilt-hat/examples/smooth.py
 0 7  *   7   *     rm /var/log/cron.log


import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # set board mode to Broadcom
GPIO.setup(18, GPIO.OUT) # set up pin 18
GPIO.output(18, 0) # turn off laser

Laser plugged into Ground and PWM pins on the Pimoni PAN-TILT Hat


