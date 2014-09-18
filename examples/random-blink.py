"""
This example will blink an LED at random
"""
import time, random, pibrella

while True:
  with random.choice(pibrella.light) as l: # Pick a random light
    l.on()
    time.sleep(0.5)
    l.off()
    time.sleep(0.5)
