from picamera import PiCamera
from datetime import datetime
from time import sleep

import subprocess

with open('cam.sh', 'rb') as file:
    script = file.read()
rc = subprocess.call(script, shell=True)

#camera = PiCamera()
# camera.led = True
#camera.rotation = 180
#camera.brightness = 50
#camera.framerate = 180
#camera.exposure_mode = 'auto'
#camera.resolution = (640, 480)
#camera.start_preview()
#camera.annotate_text = "Hi Pi!"
#camera.start_recording('./test2.h264')
#sleep(10)
#camera.stop_recording()
#camera.stop_preview()

# raspivid -w 840 -h 650 -fps 240 -o testingFps240.h264 -pts timecodes.txt -t 10000 -rot 180 -a 12 -sh 50 -br 25 -sh 25 -b 100000000
