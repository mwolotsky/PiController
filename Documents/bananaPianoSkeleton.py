import sys		 # Library needed to use sys.exit(1) from line 14
import time		 # Library needed to use time.sleep(0.1) from line 72
import pygame	 # Library needed to play the piano sounds through the speaker
import Adafruit_MPR121.MPR121 as MPR121		# Library needed to use the functions necessary to interact with the sensor

print 'BANANA PIANO TIME!!!'

# We created the "sensor" variable to interact with the Touch Hat sensor in our code 
sensor = MPR121.MPR121()

# Checks if the sensor and Raspberry Pi are properly connected
if not sensor.begin():
    print 'Error! The sensor and Raspberry Pi are not properly connected. Check your wiring!'
    sys.exit(1)
	
#--------------------------------------------------------------------------------------
# Like the sensor, if we want to interact with the sounds we have to set up the sound system.
# 1) First, use the function that sets up the sound system.      
# 2) Then, initialize the sound system.
pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()

# Sounds are stored in .wav files (sound files).
# 3) To make sounds we have to convert the .wav file into a sound! We need a total of 6 sounds.
sounds = [  <insert here>  ]

# 4) Set the volume for each of the 6 sounds. Hint: you need to go through all six sounds!


# This is an instruction to tell the user how to quit the program.
print 'Press Ctrl-C to quit.'

# Try-except, handles the errors when exiting from the infinite loop.
try:
	# 5) Create an infinite loop to continuously check which sensor pins are being touched.
	while True:
    # 6) Check each pin to see if it is being touched.
			# IF IT IS BEING TOUCHED: a) Print "Pin # is being touched"
			#						  b) Play the sound
			# IF NOT: a) Check the next pin
		
		
	
		
		
		
		
		

		# This is a delay so sounds don't overlap when they play.	
		time.sleep(0.1)
except:
	# This print statement will display the "Crtl-C" we used to exit the program.
	print