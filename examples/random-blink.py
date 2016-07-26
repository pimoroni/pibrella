#!/usr/bin/env python

import random
import time

import pibrella


"""
This example will blink an LED at random
"""

while True:
  with random.choice(pibrella.light) as l: # Pick a random light
    l.on()
    time.sleep(0.5)
    l.off()
    time.sleep(0.5)
