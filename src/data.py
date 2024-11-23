import re

class Data():
    # all temps in celcius
    _temp = 33.0
    _cool = 20.0
    _heat = 35.0
    _hum = 50.0

    _temp_lbl_type = "F"
    _temp_set_type = "F"

    _fan_cool = False
    _fan_heat = False 
    _door = True 
    _locked = True
    
    _servoLocked = True
    _out_lights = False
    _in_lights = False
    once_out_lights = False
    once_in_lights = False
    once_door = True

    def _is_float(string):
        pattern = r"^[-+]?[0-9]*\.?[0-9]+$"
        match = re.match(pattern, string)
        return bool(match)

    def _fahrenheit(c):
        return (c * 9/5) + 32
    
    def _celcius(f):
        return (f - 32) * 5 / 9    

    def set_temp(value):
        Data._temp = value

        Data._fan_cool = False
        Data._fan_heat = False

        if Data._temp < Data._cool:
            Data.fan_heat = True

        if Data._temp > Data._heat:
            Data.fan_cool = True

    def set_temp_lbl_type(value):
        Data._temp_lbl_type = value

    def set_temp_set_type(value):
        Data._temp_set_type = value

    def set_cool(value):
        if isinstance(value, str):
            s_value = str(value)
        else:
            s_value = value.get()

        if not Data._is_float(s_value):
            return
        
        f_value = float(s_value)

        if Data._temp_set_type == "F" and f_value < Data._fahrenheit(Data._heat):
            Data._cool = Data._celcius(f_value)
            if not isinstance(value, str):
                value.set("")
        elif Data._temp_set_type == "C" and f_value < Data._heat:
            Data._cool = f_value
            if not isinstance(value, str):
                value.set("")

    def set_heat(value):
        if isinstance(value, str):
            s_value = str(value)
        else:
            s_value = value.get()

        if not Data._is_float(s_value):
            return
        
        f_value = float(s_value)

        if Data._temp_set_type == "F" and f_value > Data._fahrenheit(Data._cool):
            Data._heat = Data._celcius(f_value)
            if not isinstance(value, str):
                value.set("")
        elif Data._temp_set_type == "C" and f_value > Data._cool:
            Data._heat = f_value
            if not isinstance(value, str):
                value.set("")
    
    def set_hum(value):
        Data._hum = value

    def set_locked(value):
        Data._locked = value

    def set_door(value):
        Data._door = value

    def set_in_lights(value):
        Data._in_lights = value

    def set_out_lights(value):
        Data._out_lights = value

    def get_temp():
        if Data._temp_lbl_type == "F":
            return Data._fahrenheit(Data._temp)
        else:
            return Data._temp
        
    def get_temp_str():
        return str(round(Data.get_temp(), 2))
        
    def get_temp_lbl_type():
        return Data._temp_lbl_type
    
    def get_temp_set_type():
        return Data._temp_set_type

    def get_cool():
        if Data._temp_set_type == "F":
            return Data._fahrenheit(Data._cool)
        else:
            return Data._cool
        
    def get_cool_str():
        return str(round(Data.get_cool(), 2))

    def get_heat():
        if Data._temp_set_type == "F":
            return Data._fahrenheit(Data._heat)
        else:
            return Data._heat
        
    def get_heat_str():
        return str(round(Data.get_heat(), 2))
    
    def get_hum():
        return Data._hum
    
    def get_hum_str():
        return str(round(Data.get_hum(), 2))
    
    def get_in_lights():
        return Data._in_lights
    
    def get_out_lights():
        return Data._out_lights
    
    def get_locked():
        return Data._locked
    
    def get_locked_str():
        return "Lock" if Data.get_locked() else "Unlock"

    def get_door_string():
        if Data._door:
            return "Closed"
        else:
            return "Open"
        
    def get_door():
        return Data._door