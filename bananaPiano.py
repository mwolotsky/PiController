import sys
import time
import pygame

import Adafruit_MPR121.MPR121 as MPR121

print 'BANANA PIANO TIME!'

cap = MPR121.MPR121()

if not cap.begin():
    print 'Error initializing MPR121.  Check your wiring!'
    sys.exit(1)

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()

sounds = [pygame.mixer.Sound('/home/pi/Music/A.wav'),
	  pygame.mixer.Sound('/home/pi/Music/B.wav'),
	  pygame.mixer.Sound('/home/pi/Music/D.wav'),
          pygame.mixer.Sound('/home/pi/Music/E.wav'),
          pygame.mixer.Sound('/home/pi/Music/Fsharp.wav'),
          pygame.mixer.Sound('/home/pi/Music/G.wav')]

for i in range(6):
        sounds[i].set_volume(1);

print 'Press Ctrl-C to quit.'

try:
	while True:
		if cap.is_touched(0):
        		print 'Pin 0 is being touched!'
			sounds[0].play()
		
		if cap.is_touched(1):
			print 'Pin 1 is being touched!'
			sounds[1].play()

		if cap.is_touched(2):
			print 'Pin 2 is being touched!'
			sounds[2].play()

		if cap.is_touched(3):
			print 'Pin 3 is being touched!'
			sounds[3].play()

		if cap.is_touched(4):
			print 'Pin 4 is being touched!'
			sounds[4].play()

		if cap.is_touched(5):
			print 'Pin 5 is being touched!'
			sounds[5].play()

		if cap.is_touched(6):
			print 'Pin 6 is being touched!'
			sounds[6].play()

		time.sleep(0.1)
except:
	print
