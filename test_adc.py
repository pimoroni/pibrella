from time import sleep
import pibrella



pib = pibrella.pibrella()
pib.enableADC()

while True:
  print pib.analog(0)
  sleep(0.5)

