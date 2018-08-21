#!/usr/bin/env python

import i2cdev
import time
from i2cdev import I2C

bus = I2C(1)
bus.write([0x22], addr=0x0f)
time.sleep(0.2)
d = bus.read(4, addr=0x0f)
print("Version: %d.%d\n" % (d[1], d[2]))

bus.write([0xd0], addr=0x0f)
time.sleep(0.2)
d = bus.read(3, addr=0x0f)
print("Voltage: %d mV\n" % (d[1] + d[2] * 256))

bus.write([0xd3], addr=0x0f)
time.sleep(0.2)
d = bus.read(3, addr=0x0f)
print("Voltage: %d mV\n" % (d[1] + d[2] * 256))

