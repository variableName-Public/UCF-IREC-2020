#!/bin/bash
raspivid -w 840 -h 650 -fps 240 -o testingFps240.h264 -pts timecodes.txt -t 10000 -rot 180 -a 12 -sh 50 -sh 25 -b 100000000