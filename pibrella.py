import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.OUT) # Red led
GPIO.setup(17, GPIO.OUT) # Yellow led
if GPIO.RPI_REVISION == 1:
  GPIO.setup(21, GPIO.OUT) # Green for Rev 1 boards
else:
  GPIO.setup(27, GPIO.OUT) # Green for Rev 2 boards

GPIO.setup(11, GPIO.IN) # Button


GPIO.setup(10, GPIO.IN) # Inputs
GPIO.setup(9, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(7, GPIO.IN)

GPIO.setup(25, GPIO.OUT) # Outputs
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)




class pibrella:

  def __init__(self):
    self.enablepwm = 0

  def enableTGRT(self,value):
    GPIO.setup(value, GPIO.IN)

  def detectTGRT(self,value):
    if(GPIO.input(value) == 1):
      return 1
    else:
      return 0
	 

  def enablePWM(self):
    self.PWM25 = GPIO.PWM(25, 100)
    self.PWM25.start(0)
    self.PWM24 = GPIO.PWM(24, 100)
    self.PWM24.start(0)
    self.PWM23 = GPIO.PWM(23, 100)
    self.PWM23.start(0)
    self.PWM22 = GPIO.PWM(22, 100)
    self.PWM22.start(0)
    self.enablepwm = 1

  def enableADC(self):
    print "Enabling ADC"
    GPIO.setup(10, GPIO.OUT) # MOSI
    GPIO.setup(9, GPIO.IN) # MISO
    GPIO.setup(8, GPIO.OUT) # CLK
    GPIO.setup(7, GPIO.OUT) # CS



  def red(self, value):
    if value == "on" or value == 1:
      GPIO.output(4, GPIO.HIGH)
    else:
      GPIO.output(4, GPIO.LOW)

  def yellow(self, value):
    if value == "on" or value == 1:
      GPIO.output(17, GPIO.HIGH)
    else:
      GPIO.output(17, GPIO.LOW)

  def green(self, value):
    if value == "on" or value == 1:
      GPIO.output(27, GPIO.HIGH)
    else:
      GPIO.output(27, GPIO.LOW)


  def button(self):
    if GPIO.input(11):
      return 1
    else:
      return 0


  def input10(self):
    if GPIO.input(10):
      return 1
    else:
      return 0

  def input9(self):
    if GPIO.input(9):
      return 1
    else:
      return 0

  def input8(self):
    if GPIO.input(8):
      return 1
    else:
      return 0

  def input7(self):
    if GPIO.input(7):
      return 1
    else:
      return 0


  def output25(self, value):
    if self.enablepwm == 1:
      if value == "on":
        self.PWM25.ChangeDutyCycle(100)
      else:
        self.PWM25.ChangeDutyCycle(value)
    else:
      if value == "on" or value == 1:
        GPIO.output(25, GPIO.HIGH)
      else:
        GPIO.output(25, GPIO.LOW)

  def output24(self, value):
    if self.enablepwm == 1:
      if value == "on":
        self.PWM24.ChangeDutyCycle(100)
      else:
        self.PWM24.ChangeDutyCycle(value)
    else:
      if value == "on" or value == 1:
        if value == "on" or value == 1:
          GPIO.output(24, GPIO.HIGH)
        else:
          GPIO.output(24, GPIO.LOW)

  def output23(self, value):
    if self.enablepwm == 1:
      if value == "on":
        self.PWM23.ChangeDutyCycle(100)
      else:
        self.PWM23.ChangeDutyCycle(value)
    else:
      if value == "on" or value == 1:
        if value == "on" or value == 1:
          GPIO.output(23, GPIO.HIGH)
        else:
          GPIO.output(23, GPIO.LOW)

  def output22(self, value):
    if self.enablepwm == 1:
      if value == "on":
        self.PWM22.ChangeDutyCycle(100)
      else:
        self.PWM22.ChangeDutyCycle(value)
    else:
      if value == "on" or value == 1:
        if value == "on" or value == 1:
          GPIO.output(22, GPIO.HIGH)
        else:
          GPIO.output(22, GPIO.LOW)



  def readADC(adcnum, clockpin=8, mosipin=10, misopin=9, cspin=7):
# borrowed from Adafruit :)
    if ((adcnum > 7) or (adcnum < 0)):
      return -1
    GPIO.output(cspin, True)
 
    GPIO.output(clockpin, False) # start clock low
    GPIO.output(cspin, False) # bring CS low
 
    commandout = adcnum
    commandout |= 0x18 # start bit + single-ended bit
    commandout <<= 3 # we only need to send 5 bits here
    for i in range(5):
      if (commandout & 0x80):
        GPIO.output(mosipin, True)
      else:
        GPIO.output(mosipin, False)
      commandout <<= 1
      GPIO.output(clockpin, True)
      GPIO.output(clockpin, False)
 
    adcout = 0
# read in one empty bit, one null bit and 10 ADC bits
    
    for i in range(12):
      GPIO.output(clockpin, True)
      GPIO.output(clockpin, False)
      adcout <<= 1
      if (GPIO.input(misopin)):
        adcout |= 0x1
 
    GPIO.output(cspin, True)
    adcout >>= 1 # first bit is 'null' so drop it
    return adcout




  def cleanup(self):
    GPIO.cleanup()

