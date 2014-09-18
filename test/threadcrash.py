import pibrella
for x in range(0,1000):
	pibrella.buzzer.fail()
	pibrella.buzzer.success()
	pibrella.lights.pulse()
