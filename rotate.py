from time import sleep
print("Waiting for controller")
sleep(10)

from gpiozero.pins.pigpio import PiGPIOFactory
from inputs import get_gamepad
from gpiozero import Servo

factory = PiGPIOFactory()
servo1 = Servo(18, min_pulse_width=0.0005, max_pulse_width=0.0025, pin_factory=factory)
servo2 = Servo(19, min_pulse_width=0.0005, max_pulse_width=0.0025, pin_factory=factory)

BTN_A = "BTN_SOUTH"  # button A
STATE = -1
SPEED = 0.02

values = [item/100 for item in range(-100, 100)]

def rotate():
    global STATE
    if STATE == -1:
        print("Rotate: max")
        for v in values:
            servo1.value = -1 * v
            servo2.value = v
            sleep(SPEED)
        STATE = 1
        sleep(1)
    else:
        print("Rotate: min")
        for v in values:
            servo1.value = v
            servo2.value = -1 * v
            sleep(SPEED)
        STATE = -1
        sleep(1)
        

while True:
    events = get_gamepad()
    for event in events:
        if event.code == BTN_A and event.state == 1:
            rotate()
