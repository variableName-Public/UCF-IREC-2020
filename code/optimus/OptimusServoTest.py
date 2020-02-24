import RPi.GPIO as GPIO
import time

servoPIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization
try:
    while True:
        p.ChangeDutyCycle(7.5) #  Move to 0 degree position.
        time.sleep(0.5)
        p.ChangeDutyCycle(10) # Move to 30 degree position.
        time.sleep(0.5)
        p.ChangeDutyCycle(12.5) # Move to 60 degree position.
        time.sleep(0.5)
        p.ChangeDutyCycle(15) # Move to 90 degree position.
        time.sleep(0.5)
        p.ChangeDutyCycle(2.5) # Move to -180 degree position.
        time.sleep(0.5)
except KeyboardInterrupt: # Interrupt == ctrl+z
    p.stop()
    GPIO.cleanup()
