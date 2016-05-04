#!/bin/sh

mv /home/pi/Documents /home/pi/python_games/Documents
cp -r Documents/ /home/pi/Documents
yes | sudo apt-get install jedit
jedit /home/pi/Documents/bananaPianoSkeleton.py &
sudo python /home/pi/Adafruit_Python_MPR121/examples/bananaPiano.py

