from __future__ import print_function
from gpiozero.pins.pigpio import PiGPIOFactory
from inputs import get_gamepad
from gpiozero import Servo
from time import sleep

factory = PiGPIOFactory()
servo = Servo(18, min_pulse_width=0.0005, max_pulse_width=0.0025, pin_factory=factory)
servo.min()

BTN_A = "BTN_SOUTH"  # button A
STATE = -1


def rotate():
    global STATE
    if STATE == -1:
        print("Rotate: max")
        servo.max()
        STATE = 1
        sleep(1)
    else:
        print("Rotate: min")
        servo.min()
        STATE = -1
        sleep(1)
        

while True:
    events = get_gamepad()
    for event in events:
        if event.code == BTN_A and event.state == 1:
            rotate()