# susv_python
S.USV python library

additional library needed: i2cdev from https://github.com/cbeytas/i2cdev

reads data from S.USV ( http://www.s-usv.de ) like version, input voltage, battery voltage

usage example:

#!/usr/bin/env python

from SUSV import SUSV

susv = SUSV()
print("SUSV Firmware: %s" % susv.get_version())

