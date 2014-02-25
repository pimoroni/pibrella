import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import pibrella, time

print "\nPulsing Lights"
pibrella.light.on()
time.sleep(1)
pibrella.light.off()

print "\nReading Inputs"
pibrella.input.read()

print "\nWriting Outputs"
pibrella.output.write(1)
time.sleep(1)
pibrella.output.write(0)

print "\nBuzzing Buzzer"
pibrella.buzzer.fail()

def test_e(pin):
	print "Input A: " + str(pin.read())
	pibrella.output.e.write(pin.read())

def test_f(pin):
	print "Input B: " + str(pin.read())
	pibrella.output.f.write(pin.read())

def test_g(pin):
	print "Input C: " + str(pin.read())
	pibrella.output.g.write(pin.read())

def test_h(pin):
	print "Input D: " + str(pin.read())
	pibrella.output.h.write(pin.read())

print "\nSetting up event detection"
print "Bridge an input to light output"

pibrella.input.a.changed(test_e)
pibrella.input.b.changed(test_f)
pibrella.input.c.changed(test_g)
pibrella.input.d.changed(test_h)

print "\nPress button or Ctrl+C to exit"

def do_exit(pin):
	exit()

pibrella.button.pressed(do_exit)

pibrella.pause()
