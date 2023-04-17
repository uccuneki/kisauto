from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause
from inputs import get_gamepad

factory = PiGPIOFactory()

LJ = "ABS_X"  # left joystick
NORM = 364*91

def steering():
    while True:
        events = get_gamepad()
        for event in events:
            if event.code == LJ:
                #print(str(f"Steering: {round(event.state/float(NORM), 2)}"))
                yield round(event.state/float(NORM), 2)


servo = Servo(18, min_pulse_width=0.0005, max_pulse_width=0.0025, pin_factory=factory)
servo.source = steering()
servo.source_delay = 0.01

pause()
