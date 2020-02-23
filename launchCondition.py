import RPi.GPIO as GPIO
import time

def someFUNC(i):
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(18, GPIO.OUT)
  while (i):
      print ("Launch Detected!!!")
      #print ("LED on")
      GPIO.output(18, GPIO.HIGH)
      time.sleep(0.025)
      #print ("LED off")
      GPIO.output(18, GPIO.LOW)
      time.sleep(0.025)