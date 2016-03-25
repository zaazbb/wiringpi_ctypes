# by jf
# zaazbb <zaazbb@163.com>
# https://github.com/zaazbb/libwiringpi_ctypes

from ctypes import *


_libwiringpi = CDLL('/usr/lib/libwiringPi.so')



# wiringPi.h

wiringPiSetup = _libwiringpi.wiringPiSetup
wiringPiSetup.restype = c_int
wiringPiSetup.argtype = []


pinMode = _libwiringpi.pinMode
pinMode.restype = None
pinMode.argtype = [c_int, c_int]

pullUpDnControl = _libwiringpi.pullUpDnControl
pullUpDnControl.restype = None
pullUpDnControl.argtype = [c_int, c_int]

digitalRead = _libwiringpi.digitalRead
digitalRead.restype = c_int
digitalRead.argtype = [c_int]

digitalWrite = _libwiringpi.digitalWrite
digitalWrite.restype = None
digitalWrite.argtype = [c_int, c_int]


wiringPiISR_ = _libwiringpi.wiringPiISR
wiringPiISR_.restype = c_int
wiringPiISR_function = CFUNCTYPE(None)
wiringPiISR_.argtype = [c_int, c_int, wiringPiISR_function]




# wiringPiSPI.h

wiringPiSPIDataRW = _libwiringpi.wiringPiSPIDataRW
wiringPiSPIDataRW.restype = c_int
wiringPiSPIDataRW.argtype = [c_int, POINTER(c_ubyte), c_int]

wiringPiSPISetup = _libwiringpi.wiringPiSPISetup
wiringPiSPISetup.restype = c_int
wiringPiSPISetup.argtype = [c_int, c_int]
