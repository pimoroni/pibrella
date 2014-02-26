import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import pibrella, time, signal

# Pulse all of the lights

TIME_ON = 0.2
TIME_OFF = 0.2
FADE_ON = 0.2
FADE_OFF = 0.2

# Play a siren

siren_stopped = True

def siren():
	if siren_stopped == True:
		pibrella.buzzer.stop()
		return True
	for x in xrange(-30,30,2):
		pibrella.buzzer.note(x)
		time.sleep(0.01)
	for x in reversed(xrange(-30,30,2)):
		pibrella.buzzer.note(x)
		time.sleep(0.01)


pibrella.async_start('siren',siren)

def start_siren():
	global siren_stopped
	siren_stopped = False
	pibrella.light.pulse(TIME_ON, TIME_OFF, FADE_ON, FADE_OFF)

def stop_siren():
	global siren_stopped
	siren_stopped = True
	pibrella.light.stop()

def handle_button(button):
	global siren_stopped
	if siren_stopped == True:
		start_siren()
		print "Starting Siren"
	else:
		stop_siren()
		print "Stopping Siren"

pibrella.button.released(handle_button)

# Sleep for 20 seconds

#time.sleep(20)

signal.pause()

# Exit!
