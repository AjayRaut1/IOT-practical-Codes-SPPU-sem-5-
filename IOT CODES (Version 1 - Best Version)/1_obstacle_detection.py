# 1.Write an application to detect obstacle and notify user using LEDs

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.IN)

try:
    while True:
        i= GPIO.input(3)
        if i==1:
            print("No Obstacle")
            time.sleep(0.1)
    else:
        print("Obstacle Found")
        time.sleep(0.1)