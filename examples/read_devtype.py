try:
    from libwiringpi.wiringpi import *
except ImportError:
    import sys
    sys.path.append('..')
    from libwiringpi.wiringpi import *


def rreg(addr):
    buf = bytes([addr, 0xFF])
    wiringPiSPIDataRW(0, buf, 2)
    return buf[1]

if __name__ == '__main__':
"""
expact outputs:

devtype = 08.
devver = 06.
devtype = 08.
devver = 06.
devtype = 08.
devver = 06.
"""
    wiringPiSPISetup(0, 500000)
    for i in range(3):
        c = 0
        c = rreg(0)
        print("devtype = %02X."% c)
        c = 0
        c = rreg(1)
        print("devver = %02X."% c)
