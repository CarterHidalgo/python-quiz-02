import RPi.GPIO as GPIO
from data import Data
import dht11, time

class Circuit():
    UI = None

    REDPIN = 15
    BLUEPIN = 19
    GREENPIN = 21
    WHITEPIN = 23

    DOORPIN = 7
    DHTPIN = 37
    SERVOPIN = 11

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    GPIO.setup(REDPIN, GPIO.OUT)
    GPIO.setup(BLUEPIN, GPIO.OUT)
    GPIO.setup(GREENPIN, GPIO.OUT)
    GPIO.setup(WHITEPIN, GPIO.OUT)
    GPIO.setup(DOORPIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(SERVOPIN, GPIO.OUT)

    GPIO.output(REDPIN, GPIO.LOW)
    GPIO.output(BLUEPIN, GPIO.LOW)
    GPIO.output(GREENPIN, GPIO.LOW)
    GPIO.output(WHITEPIN, GPIO.LOW)
    
    SERVO = GPIO.PWM(SERVOPIN, 50)
    SERVO.start(0)

    def set_angle(angle):
        print("angle: " + str(angle))
        cycle = 2.5 + (angle / 18)
        Circuit.SERVO.ChangeDutyCycle(cycle)
        time.sleep(0.7)
        Circuit.SERVO.ChangeDutyCycle(0)

    def run(ui, terminate):
        Circuit.UI = ui

        while not terminate.is_set():
            Circuit._read_sensors()
            Circuit._update_with_data()
        
        Circuit.SERVO.stop()
        GPIO.cleanup()
        print("circuit terminated")

    def _read_sensors():
        Data.set_door(False if GPIO.input(Circuit.DOORPIN) == GPIO.HIGH else True)

        if (Data.get_door() != Data.once_door) and not Data.get_locked():
            if GPIO.input(Circuit.DOORPIN) == GPIO.HIGH:
                Data.set_door(False)
            else:
                Data.set_door(True)
            Data.once_door = Data.get_door()
            Circuit.UI.update()
        
        instance = dht11.DHT11(pin=Circuit.DHTPIN)
        result = instance.read()
        if result.is_valid():
            Data.set_temp(result.temperature)
            Data.set_hum(result.humidity)


    def _update_with_data():
        if Data._fan_cool:
            GPIO.output(Circuit.BLUEPIN, GPIO.HIGH)
        else:
            GPIO.output(Circuit.BLUEPIN, GPIO.LOW)
        
        if Data._fan_heat:
            GPIO.output(Circuit.REDPIN, GPIO.HIGH)
        else:
            GPIO.output(Circuit.REDPIN, GPIO.LOW)

        if Data.get_door():
            if Data.get_locked() != Data._servo_locked:
                if Data.get_locked():
                    Circuit.set_angle(0)
                else:
                    Circuit.set_angle(90)
                Data._servo_locked = Data.get_locked()

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
