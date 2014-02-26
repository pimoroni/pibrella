import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import pibrella, time, random

scores = []
current_light = 'green'
red_time = 0

def handle_reaction(pin):
	global current_light, red_time
	if current_light == 'red':
		speed = time.time() - red_time
		print("Yay, red light!")
		print("You took: " + str(speed) + "sec!")
		scores.append(speed)
		current_light = 'green'
		random_lights()
	else:
		print("Woah, woah, too soon!")

pibrella.button.pressed(handle_reaction,20)

def random_lights():
	global current_light, red_time
	print("Light going green!")
	pibrella.light.green.on()
	pibrella.light.red.off()
	current_light = 'green'
	delay = random.randint(1,5)
	time.sleep(delay)
	print("Light going amber!")
	pibrella.light.amber.on()
	pibrella.light.green.off()
	current_light = 'amber'
	time.sleep(0.5)
	print("Light going red!")
	pibrella.light.red.on()
	pibrella.light.amber.off()
	red_time = time.time()
	current_light = 'red'

random_lights()

pibrella.pause()
