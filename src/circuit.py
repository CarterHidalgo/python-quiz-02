# import RPi.GPIO as GPIO
from data import Data

class Circuit():
    REDPIN = 15
    BLUEPIN = 19
    GREENPIN = 21
    WHITEPIN = 23

    # GPIO.setmode(GPIO.BOARD)
    # GPIO.setup(REDPIN, GPIO.OUT)
    # GPIO.setup(BLUEPIN, GPIO.OUT)
    # GPIO.setup(GREENPIN, GPIO.OUT)
    # GPIO.setup(WHITEPIN, GPIO.OUT)

    def run():
        Circuit._read_sensors()
        Circuit._update_with_data()

    def _read_sensors():
        return

    def _update_with_data():


        return

        if Data.fan_cool:
            print("blue")
        
        if Data.fan_heat:
            print("red")

        if Data.doorIsClosed():
            if Data.locked and not Data.servoLocked:
                print("lock servo")
                Data.servoLocked = True
            elif not Data.locked and Data.servoLocked:
                print("unlock servo")
                Data.servoLocked = False

        if Data.out_lights and not Data.real_out:
            print("out lights on")
            Data.real_out = True
        elif not Data.out_lights and Data.real_out:
            print("out lights off")
            Data.real_out = False

        if Data.in_lights and not Data.real_in:
            print("in lights on")
            Data.real_in = True
        elif not Data.in_lights and Data.real_in:
            print("in lights off")
            Data.real_in = False