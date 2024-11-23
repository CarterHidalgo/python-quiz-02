import RPi.GPIO as GPIO
from data import Data
from tkui import TKUI

class Circuit():
    UI = None

    REDPIN = 15
    BLUEPIN = 19
    GREENPIN = 21
    WHITEPIN = 23

    DOORPIN = 7

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    GPIO.setup(REDPIN, GPIO.OUT)
    GPIO.setup(BLUEPIN, GPIO.OUT)
    GPIO.setup(GREENPIN, GPIO.OUT)
    GPIO.setup(WHITEPIN, GPIO.OUT)
    GPIO.setup(DOORPIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.output(REDPIN, GPIO.LOW)
    GPIO.output(BLUEPIN, GPIO.LOW)
    GPIO.output(GREENPIN, GPIO.LOW)
    GPIO.output(WHITEPIN, GPIO.LOW)

    def run(ui, terminate):
        Circuit.UI = ui

        while not terminate.is_set():
            Circuit._read_sensors()
            Circuit._update_with_data()
        
        GPIO.cleanup()
        print("circuit terminated")

    def _read_sensors():
        Data.set_door(False if GPIO.input(Circuit.DOORPIN) == GPIO.HIGH else True)

        if Data.get_door() != Data.once_door:
            if GPIO.input(Circuit.DOORPIN) == GPIO.HIGH:
                Data.set_door(False)
            else:
                Data.set_door(True)
            Data.once_door = Data.get_door()
            Circuit.UI.update()

    def _update_with_data():
        # if Data.fan_cool:
        #     print("blue")
        
        # if Data.fan_heat:
        #     print("red")

        # if Data.doorIsClosed():
        #     if Data.locked and not Data.servoLocked:
        #         print("lock servo")
        #         Data.servoLocked = True
        #     elif not Data.locked and Data.servoLocked:
        #         print("unlock servo")
        #         Data.servoLocked = False


        if Data.get_in_lights() != Data.once_in_lights:
            if Data.get_in_lights():
                GPIO.output(Circuit.GREENPIN, GPIO.HIGH)
            else:
                GPIO.output(Circuit.GREENPIN, GPIO.LOW)
            Data.once_in_lights = Data.get_in_lights()

        if Data.get_out_lights() != Data.once_out_lights:
            if Data.get_out_lights():
                GPIO.output(Circuit.WHITEPIN, GPIO.HIGH)
            else:
                GPIO.output(Circuit.WHITEPIN, GPIO.LOW)
            Data.once_out_lights = Data.get_out_lights()
