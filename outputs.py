from time import sleep
import pibrella



pib = pibrella.pibrella()

while True:
  pib.output22(1)
  sleep(5)
  pib.output22(0)
  sleep(5)
