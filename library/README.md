Pibrella
========

Support code and API library for the Pibrella addon board.

Installation
============

The easy way
------------

We've created a super-easy installation script that will install all pre-requisites and get your Pibrella up and running in a jiffy. To run it fire up Terminal which you'll find in Menu -> Accessories -> Terminal on your Raspberry Pi desktop like so:

![Finding the terminal](terminal.jpg)

In the new terminal window type the following and follow the instructions:

```bash
curl -sS get.pimoroni.com/pibrella | bash
```

If you choose to download examples you'll find them in `/home/pi/Pimoroni/pibrella`, but you can also check out the examples for Pibrella in: [examples](examples)

Alternative method
------------------

Alternatively you can clone this repository and install:

    git clone http://github.com/pimoroni/pibrella
    cd pibrella
    sudo python setup.py install

To try the examples:

    git clone http://github.com/pimoroni/pibrella
    cd pibrella/examples
    sudo python siren.py


Usage
=====

Pibrella depends upon RPi.GPIO > 0.5.4, which requires root to access your GPIO. Newer versions do not have this requirement, so feel free to try with and without 'sudo' and see what works for you.

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

You can also fade LEDs from one brightness to another, like so:

    pibrella.light.red.fade(0, 100, 2) # From 0 to 100% in 2 seconds


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

    my_value = pibrella.input.a.read()

Or to read all inputs into a dictionary:

    inputs = pibrella.input.read()
    input_a = inputs['a']


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

    pibrella.pause()

The `pibrella.pause()` command is included to prevent your program exiting immediately, since the events are handled in the background there's otherwise nothing to keep your program busy.

The "pin" parameter of the button pressed function is the Pibrella pin that triggered the event, in this case "pin" will be equal to "pibrella.button" so you can .read() it.

    def button_changed(pin):
        if pin.read() == 1:
            print("You pressed the button!")
        else:
            print("You released the button!")

    pibrella.button.changed(button_changed)

    pibrella.pause()

If you want to turn a light on when the button is pressed, your code should look something like this:

    import pibrella

    def button_changed(pin):
        pibrella.light.red.write(pin.read())

    pibrella.button.changed(button_changed)

    pibrella.pause()

And in just 5 lines, you've got started with event-driven programming!

Quick Reference
===============

All of Pibrella's inputs, outputs and lights are stored in collectons. You can reference a pin by name or by index in one of three ways:

    pibrella.light[0]        # By index
    pibrella.light['red']    # By name, for use with a variable
    pibrella.light.red       # By name

You can also refer to a whole collection at once, simply by omitting the index or name:

    pibrella.light

Help Text
---------

Pibrella has a small amount of built-in help. If you want to know the names of the lights, inputs or putputs simply type:

    pibrella.lights

Or otherwise, and you'll get a list of the supported names.

Lights
------

The following methods are available for every Pibrella light:

    .on()       # Turn a light on
    .off()      # Turn a light off
    .high()     # Same as on
    .low()      # Same as off

    .toggle() # Toggle a lights status from on to off and off to on
    # If lights are pulsing/blinking toggle will always turn them off

    .pulse( transition_on, transition_off, time_on, time_off )    # Pulse a light, values in seconds
    .blink( time_on, time_off )     # Blink a light, values in seconds
    .write( value )                 # Turn on if value = 1, or off if value = 0

Outputs
-------

An output can do everything a light can do, they are identical in all but name!

Inputs
------

The following methods are available for every Pibrella input:

General
-------

    pibrella.pause() # Wrapper for signal.pause(), great for pausing your application after calling blink, pulse or loop

    pibrella.loop( function_name )  # Pass pibrella a function to run over and over again, asyncronously
    # You must call pibrella.pause() after giving it a function to loop, or your code will simply exit!




# Changelog

1.4.1
-----

* Fixes for Python 3
* Repackaging with setup.cfg

1.4.0
-----

* Initial release to apt

1.3.1
-----

* Fixed Manifest

1.3.0
-----

* Restructured library to include pins/main code in Pibrella package
* Fix to notation support so notes are correctly played

1.2.0
-----

* Significant version bump to highlight launch to Production/Stable status
* Small tweak to allow use of with, ie: "with pibrella.light.red as red:"

1.1.7
-----

* Fixed buzzer to stop after playing melody
* Wrapped changed/pressed/released so they can be registered simultaneously
* Added "len" to pin collections, to support random.choice(pibrella.light)
* Added error if run without root

1.1.6
-----

* Populated LICENSE.txt

1.1.5
-----

* Renamed amber to yellow and added alias support for backwards-compatibility
* Added lights, inputs, outputs and pins as pluralalised aliases for light, input etc
* Tweaked how on/off/toggle calls to lights/outputs are handled during pulse/blink

1.1.4
-----

* Added pulse(), blink() and fade() to all outputs

1.1.3
-----

* Built-in asyncronous alarm sound! pibrella.buzzer.alarm()
* Replaced xrange with range

1.1.2
-----

* Added support for REV 1 Raspberry Pi

1.1.1
-----

* Added fade(from,to,duration) for lights

1.1.0
-----

* Removed *.all.* keyword, use pibrella.input.read() instead of pibrella.input.all.read()
* Added helper to list pins, try: pibrella.input in interactive shell
* Added ['name'] and [idx] support to pin collections, try: pibrella.input[0] pibrella.input['a']
* Added buzzer to pibrella.pin
* Added return values to most methods

1.0.0
-----

* Initial development/beta release

