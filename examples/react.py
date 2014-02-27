import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import pibrella, time, random

# Number of attempts we get before game over
attempts = 10

# Keep track of the score
score = 0

# Keep track of the current light colour
current_light = 'green'

# Keep track of when the light turns red
red_time = 0

# Keep track of button press
button_pressed = False

def handle_reaction(pin):
	global attempts, current_light, red_time, button_pressed, score
	if current_light == 'red':
		# Determine how long the reaction took
		speed = time.time() - red_time
	
		# Update the score
		score = score + (2 - speed)
		attempts = attempts - 1

		# Feed back to user
		pibrella.buzzer.success()
		print("Yay, red light!")
		print("You took: " + str(speed) + "sec!")
		print("Score: " + str(score))		

		# Break the red light loop
		button_pressed = True
	else:
		# Whoops, the light isn't red yet1
		pibrella.buzzer.fail()
		print("Woah, woah, too soon!")
	
		# Update the score with
		# a time penalty
		score = score - 0.5
		print("Score: " + str(score))

# Set up the button pressed event with a 20ms debounce
pibrella.button.pressed(handle_reaction,20)

# Our main loop, goes from green to amber to red
# at psuedo random intervals
def random_lights():
	global attempts, current_light, red_time, button_pressed, score

	if attempts == 0:
		print("Game over!")
		print("You scored: " + str(score))
		exit()

	# Make sure we clear the button_pressed state
	button_pressed = False

	# Progress the light
	print("Light going green!")

	pibrella.light.green.on()
	pibrella.light.red.off()

	current_light = 'green'

	# Delay a random-ish amount of time
	delay = random.randint(1,5)
	time.sleep(delay)

	# Progress the light
	print("Light going amber!")
	
	pibrella.light.amber.on()
	pibrella.light.green.off()

	current_light = 'amber'

	# Small delay
	time.sleep(0.5)

	# Progress the light
	print("Light going red!")

	current_light = 'red'
	red_time = time.time()

	pibrella.light.red.on()
	pibrella.light.amber.off()

	# Wait for the button to be pressed
	while button_pressed == False:
		time.sleep(0.1)

pibrella.loop(random_lights)

pibrella.pause()
