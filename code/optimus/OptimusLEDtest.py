import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
print ("LED on")
i = 0
while (i < 50):
    print ("LED on")
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.025)
    print ("LED off")
    GPIO.output(18, GPIO.LOW)
    time.sleep(0.025)
    i += 1
