from __future__ import print_function
import time
from dual_g2_hpmd_rpi import motors, MAX_SPEED
from inputs import get_gamepad

RT = "ABS_RZ"  # right trigger
LT = "ABS_Z"  # left trigger
NORM = 2.13


class DriverFault(Exception):
    def __init__(self, driver_num):
        self.driver_num = driver_num

def raiseIfFault():
    if motors.motor1.getFault():
        raise DriverFault(1)


try:
    motors.setSpeeds(0, 0)

    while True:
        events = get_gamepad()
        for event in events:
            if event.code == RT:
                motors.motor1.setSpeed(event.state//NORM)
                print(f"Forward: {event.state//NORM}")
            if event.code == LT:
                motors.motor1.setSpeed(-event.state//NORM)
                print(f"Backward: {event.state//NORM}")

finally:
    motors.forceStop()
