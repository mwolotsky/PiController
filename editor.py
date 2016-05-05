file = open("skeleton.py",'r+')
i = 1
List = []
for line in file:
	Str = ""
	if (i == 25):
		Str += "sounds = ["
		L = ['A','B','D','E','Fsharp','G']
		for c in L:
			Str += "pygame.mixer.Sound(\"/home/pi/%s.wav\")" % c
			if c != 'G':
				Str += ','
			else:
				Str += ']'
		List.append(Str)
	elif (i == 28):
		Str += "for i in range(6):\n"
		Str += "\tsounds[i].set_volume(1)"
		List.append(Str)
	elif (i == 41):
		for j in range(6):
			Str += "\t\tif sensor.is_touched(%d):\n" % j
			Str += "\t\t\tprint \"Pin %d is being touched!\"\n" % j
			Str += "\t\t\tsounds[%d].play()\n" % j
		List.append(Str)
	else:
		List.append(line)
	i += 1
file.close()
file = open('filledSkeleton.py','w')
for line in List:
	file.write(line)
file.close()

			
