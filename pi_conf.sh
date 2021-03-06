#!/bin/bash

sudo apt-get update
yes | sudo apt-get install build-essential python-dev python-smbus python-pip git
sudo apt-get clean
cd ~
git clone https://github.com/adafruit/Adafruit_Python_MPR121.git

cd Adafruit_Python_MPR121
sudo python setup.py install

cd ~/PiController

cp Music/* ~/Music/
mv /home/pi/Documents /home/pi/python_games/Documents
cp bananaPiano.py /home/pi/Adafruit_Python_MPR121/examples/
cp -r Documents/ /home/pi/Documents
yes | sudo apt-get install jedit
sudo apt-get clean
jedit /home/pi/Documents/bananaPianoSkeleton.py &
sudo python /home/pi/Adafruit_Python_MPR121/examples/bananaPiano.py
