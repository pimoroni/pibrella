import pibrella

print "\nPulsing Lights"
pibrella.light.pulse(1,1,1,1)

print "\nReading Inputs"
pibrella.input.read()

print "\nWriting Outputs"
pibrella.output.write(1)

print "\nBuzzing Buzzer"
pibrella.buzzer.fail()

print "\nPress button or Ctrl+C to exit"

def do_exit(pin):
	exit()

pibrella.button.pressed(do_exit)

pibrella.pause()
