Pibrella
========

Support code and API libreary for the Pibrella addon board.

Usage
=====


Run as root!
------------

Pibrella depends upon RPi.GPIO > 0.5.4, which requires root to access your GPIO.

If you're using an interactive shell you should: sudo python -i, otherwise sudo python yourscript.py

First steps
-----------

To get started you need to import pibrella. Simply:

    import pibrella

This will set up GPIO for you and collect all of the Pibrella's inputs and outputs into some handily named objects.

If, for example, you wanted to turn on an LED you could:

    pibrella.light.red.on()

And to turn it off again:

    pibrella.light.red.off()

Pibrellas collections ( lights, inputs, outputs ) allow you to also control a group of things at the same time. So to turn all of the LEDs off you can simply:

    pibrella.light.off()

Or on:

    pibrella.light.on()


Blinking and pulsing LEDs
-------------------------

Lights aren't simply there for toggling on and off. Any good lighting display needs pulsing, fading, blinking and strobing. Pibrella has functions for those, too:

    pibrella.light.red.blink(ON_TIME, OFF_TIME) 

And something more exciting:

    pibrella.light.red.pulse(FADE_IN_TIME, FADE_OUT_TIME, ON_TIME, OFF_TIME)

The astute observer will realise that these are equivilent:

    pibrella.light.red.pulse(0, 0, 1, 1)
    pibrella.light.red.blink(1, 1)

Inputs and outputs
------------------

The input and output collections correspond to the 4 in and 4 out pins of the Pibrella. These are named a, b, c, d for inputs and e, f, g, h for outputs- you'll see these labels on the board itself.

To turn output "e" on, you can:

    pibrella.output.e.on()

You can also write an explicit value, ( 1 is on/high, 0 is off/low ) like so

    pibrella.output.e.write(1)

This is useful if you want to toggle a pin on and off programmatically, or write an input value directly to an output.

And you can write to the whole output collection simultaneously if you wish:

    pibrella.output.write(1)

Inputs are similar, except you're reading them instead of turning them on and off. To read a single input:

    my_value = pibrella.input.e.read()

Or to read all inputs into a dictionary:

    inputs = pibrella.input.read()
    input_e = inputs['e']


The button
----------

The Pibrella button is, for all intents and purposes, just another input. It does, however, have a pull-down resistor enabled to prevent it reading random electrical fluctuations as button presses.

Like an input, you can read the button state at any time:

    pibrella.button.read()

The buzzer
----------

The buzzer is just another output. However just turning it on and off wont get you much more than a single pop, it needs to be toggled rapidly to make a continuous tone. We've provided functions for this.

First, you can buzz at a specific frequency:

    pibrella.buzzer.buzz( frequency )
    
Or play a note ( you can use both positive and negative values here, with 0 being A at 440Hz )

    pibrella.buzzer.note( 1 )

Or play a built-in tone:

    pibrella.buzzer.fail()
    pibrella.buzzer.success()


Handling events
---------------

If you want to catch an input changing state and run a specific function, you can use changed, pressed and released on any of the inputs or the button. Changed will trigger when a pin transitions from 1 ( high/on ) to 0 ( low/off ) or vice versa. Pressed will trigger when it transitions from 0 to 1, and Released when it transitions from 1 to 0.

For example:

    def button_pressed(pin):
        print("You pressed the button!")

    pibrella.button.pressed(button_pressed)

The "pin" parameter of the button pressed function is the Pibrella pin that triggered the event, in this case "pin" will be equal to "pibrella.button" so you can .read() it.

    def button_changed(pin):
        if pin.read() == 1:
            print("You pressed the button!")
        else:
            print("You released the button!")

    pibrella.button.changed(button_changed)

If you want to turn a light on when the button is pressed, your code should look something like this:

    import pibrella

    def button_changed(pin):
        pibrella.light.red.write(pin.read())

    pibrella.button.changed(button_changed)

And in just 4 lines, you've got started with event-driven programming!

