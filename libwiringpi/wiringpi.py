# by jf
# zaazbb <zaazbb@163.com>
# https://github.com/zaazbb/libwiringpi_ctypes

from _wiringpi import *


(
    INPUT,
    OUTPUT,
    PWM_OUTPUT,
    GPIO_CLOCK,
    SOFT_PWM_OUTPUT,
    SOFT_TONE_OUTPUT,
    PWM_TONE_OUTPUT
) = range(7)

(LOW, HIGH) = (0, 1)

(PUD_OFF, PUD_DOWN, PUD_UP) = (0, 1, 2)

(INT_EDGE_SETUP, INT_EDGE_FALLING, INT_EDGE_RISING, INT_EDGE_BOTH) = range(4)


def wiringPiISR(pin, mode, function):
    return wiringPiISR_(pin, mode, wiringPiISR_function(function))
