# by jf
# zaazbb <zaazbb@163.com>
# https://github.com/zaazbb/libwiringpi_ctypes

from ctypes import *


_libwiringpi = CDLL('/usr/lib/libwiringPi.so')



# wiringPi.h

wiringPiSetup = _libwiringpi.wiringPiSetup
wiringPiSetup.restype = c_int
wiringPiSetup.argtype = []

wiringPiSetupSys = _libwiringpi.wiringPiSetupSys
wiringPiSetupSys.restype = c_int
wiringPiSetupSys.argtype = []

wiringPiSetupGpio = _libwiringpi.wiringPiSetupGpio
wiringPiSetupGpio.restype = c_int
wiringPiSetupGpio.argtype = []

wiringPiSetupPhys = _libwiringpi.wiringPiSetupPhys
wiringPiSetupPhys.restype = c_int
wiringPiSetupPhys.argtype = []


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

pwmWrite = _libwiringpi.pwmWrite
pwmWrite.restype = None
pwmWrite.argtype = [c_int, c_int]

analogRead = _libwiringpi.analogRead
analogRead.restype = c_int
analogRead.argtype = [c_int]

analogWrite = _libwiringpi.analogWrite
analogWrite.restype = None
analogWrite.argtype = [c_int, c_int]



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
