from time import sleep
import pibrella



pib = pibrella.pibrella()

sleeptime = 0.2

while True:
  pib.output22(1)
  sleep(sleeptime)
  pib.output22(0)
  sleep(sleeptime)
  pib.output23(1)
  sleep(sleeptime)
  pib.output23(0)
  sleep(sleeptime)
  pib.output24(1)
  sleep(sleeptime)
  pib.output24(0)
  sleep(sleeptime)
  pib.output25(1)
  sleep(sleeptime)
  pib.output25(0)
  sleep(sleeptime)
