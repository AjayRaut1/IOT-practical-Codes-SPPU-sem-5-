import RPi.GPIO as GPIO
import time

sensor = 11
led = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(led,GPIO.OUT)

GPIO.output(led,False)
print("IR Sensor Ready...")
print(" ")
time.sleep(5)

try:
  while True:
    if GPIO.input(sensor):
      GPIO.output(led,False)
      print("Obstacle Detected")
      while GPIO.input(sensor):
        time.sleep(0.2)
    else:
      GPIO.output(led,True)
    
    
except KeyboardInterrupt:
  GPIO.cleanup()
  
