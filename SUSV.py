#!/usr/bin/env python

import i2cdev
import time
from i2cdev import I2C

class SUSV(object):
	def __init__(self):
		self.SUSV_ADDR = 0x0F
		self.SUSV_VOLTAGE = 0xD0
		self.SUSV_POWER_EXT = 0xD1
		self.SUSV_POWER_BAT = 0xD2
		self.SUSV_VOLTAGE_BAT = 0xD3
		self.SUSV_STATE_BAT = 0xD4
		self.SUSV_CHARGE = 0x35
		self.SUSV_VERSION = 0x22
		self.SUSV_POWER_STATE = 0x45
		self.SUSV_DELAY = 0.2
		
		self.susv = I2C(1)

	def get_version(self):
		try:
			self.susv.write([self.SUSV_VERSION], addr=self.SUSV_ADDR)
			time.sleep(self.SUSV_DELAY)
			self.data = self.susv.read(4, addr=self.SUSV_ADDR)
		except IOError:
			print("SUSV not detected")
		return str(self.data[1]) + "." + str(self.data[2])

	def get_voltage(self):
		try:
			self.susv.write([self.SUSV_VOLTAGE], addr=self.SUSV_ADDR)
			time.sleep(self.SUSV_DELAY)
			self.data = self.susv.read(3, addr=self.SUSV_ADDR)
		except IOError:
			print("SUSV not detected")
		return (self.data[1] + (self.data[2] << 8)) / 1000.0

	def get_voltage_bat(self):
		try:
			self.susv.write([self.SUSV_VOLTAGE_BAT], addr=self.SUSV_ADDR)
			time.sleep(self.SUSV_DELAY)
			self.data = self.susv.read(3, addr=self.SUSV_ADDR)
		except IOError:
			print("SUSV not detected")
		return (self.data[1] + (self.data[2] << 8)) / 1000.0
		
def main():
	susv = SUSV()
	print("SUSV Firmware:      %s" % susv.get_version())
	print("SUSV Voltage:      %6.3f" % susv.get_voltage())
	print("SUSV Bat Voltage:  %6.3f" % susv.get_voltage_bat())

if __name__ == '__main__':
	main()
