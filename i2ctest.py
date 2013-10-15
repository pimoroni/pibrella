import smbus
from time import sleep

bus = smbus.SMBus(1)

bus.write_byte_data(0x13, 0x80, 0x08)

while True:
  bus.write_byte_data(0x13, 0x80, 0x08)
  bus.write_byte_data(0x13, 0x80, 0x10)

  while bus.read_byte_data(0x13, 0x80) & 0x20 == 0x00:
    pass

  high = bus.read_byte_data(0x13, 0x87)
  low = bus.read_byte_data(0x13, 0x88)

  while bus.read_byte_data(0x13, 0x80) & 0x40 == 0x00:
    pass

  ambh = bus.read_byte_data(0x13, 0x85)
  ambl = bus.read_byte_data(0x13, 0x86)

  value = low | (high << 8)
  amb = ambl | (ambh << 8)
  print "Distance: " + str(value) + " - Ambient: " + str(amb)




#  print bus.read_i2c_block_data(0x13, 0x88, 2)
 
