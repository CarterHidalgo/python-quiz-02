from tkinter import *
from functools import partial
from data import Data

class TKUI():
    def __init__(self):
        self.root = Tk()

        self.temp_lbl_type = StringVar(value="F")
        self.temp_set_type = StringVar(value="F")
        self.cool = StringVar(value="")
        self.heat = StringVar(value="")
        self.in_lights = StringVar(value="False")
        self.out_lights = StringVar(value="False")

        self.root.geometry("500x200")
        self.root.title("Quiz 02 TK UI")

        self.rb_far = Radiobutton(self.root, text="Fahrenheit", variable=self.temp_lbl_type, value="F", command=partial(self.handle_temp_lbl_type, "F"))
        self.rb_far.grid(row=0, column=0)
        self.rb_cel = Radiobutton(self.root, text="Celcius", variable=self.temp_lbl_type, value="C", command=partial(self.handle_temp_lbl_type, "C"))
        self.rb_cel.grid(row=0, column=1)

        self.lbl_temp = Label(self.root, text=f"Temperature: {Data.get_temp()} {Data.get_temp_lbl_type()}")
        self.lbl_temp.grid(row=0, column = 2)

        self.lbl_hum = Label(self.root, text=f"Humidity: {Data.get_hum_str()}")
        self.lbl_hum.grid(row=0, column=3)

        self.rb_far_set = Radiobutton(self.root, text="Fahrenheit", variable=self.temp_set_type, value="F", command=partial(self.handle_temp_set_type, "F"))
        self.rb_far_set.grid(row=1, column=0)
        self.rb_cel_set = Radiobutton(self.root, text="Celcius", variable=self.temp_set_type, value="C", command=partial(self.handle_temp_set_type, "C"))
        self.rb_cel_set.grid(row=1, column=1)

        self.lbl_cool = Label(self.root, text=f"Cool ({Data.get_cool_str()}) {Data.get_temp_set_type()}")
        self.lbl_cool.grid(row=2, column=0, columnspan=2)

        self.en_cool = Entry(self.root, textvariable=self.cool)
        self.en_cool.grid(row=2, column=2)

        self.btn_cool = Button(self.root, text="Set Cool", command=self.handle_temp_set_cool)
        self.btn_cool.grid(row=2, column=3)

        self.lbl_heat = Label(self.root, text=f"Heat ({Data.get_heat_str()}) {Data.get_temp_set_type()}")
        self.lbl_heat.grid(row=3, column=0, columnspan=2)

        self.en_heat = Entry(self.root,textvariable=self.heat)
        self.en_heat.grid(row=3, column=2)

        self.btn_heat = Button(self.root, text="Set Heat", command=self.handle_temp_set_heat)
        self.btn_heat.grid(row=3, column=3)

        self.lbl_door = Label(self.root, text=f"Door: {Data.get_door_string()}")
        self.lbl_door.grid(row=4, column=0)

        self.btn_lock = Button(self.root, text=Data.get_locked_str(), command=self.handle_lock)
        self.btn_lock.grid(row=4, column=1, columnspan=2)

        self.lbl_in_lights = Label(self.root, text="Inside Lights")
        self.lbl_in_lights.grid(row=5, column=0)

        self.rb_in_lights_on = Radiobutton(self.root, text="On", variable=self.in_lights, value="True", command=partial(self.handle_in_lights, True))
        self.rb_in_lights_on.grid(row=5, column=1)

        self.rb_in_lights_off = Radiobutton(self.root, text="Off", variable=self.in_lights, value="False", command=partial(self.handle_in_lights, False))
        self.rb_in_lights_off.grid(row=5, column=2)

        self.lbl_out_lights = Label(self.root, text="Outside Lights")
        self.lbl_out_lights.grid(row=6, column=0)

        self.rb_out_lights_on = Radiobutton(self.root, text="On", variable=self.out_lights, value="True", command=partial(self.handle_out_lights, True))
        self.rb_out_lights_on.grid(row=6, column=1)

        self.rb_out_lights_off = Radiobutton(self.root, text="Off", variable=self.out_lights, value="False", command=partial(self.handle_out_lights, False))
        self.rb_out_lights_off.grid(row=6, column=2)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def update(self):
        self.lbl_temp.config(text=f"Temperature: {Data.get_temp_str()} {Data.get_temp_lbl_type()}")
        self.lbl_hum.config(text=f"Humidity: {Data.get_hum_str()}")

        self.lbl_cool.config(text=f"Cool ({Data.get_cool_str()}) {Data.get_temp_set_type()}")
        self.lbl_heat.config(text=f"Heat ({Data.get_heat_str()}) {Data.get_temp_set_type()}")

        self.lbl_door.config(text=f"Door: {Data.get_door_string()}")

        self.btn_lock.config(text=Data.get_locked_str())

        self.in_lights.set(str(Data.get_in_lights()))
        self.out_lights.set(str(Data.get_out_lights()))

        self.temp_lbl_type.set(Data.get_temp_lbl_type())
        self.temp_set_type.set(Data.get_temp_set_type())

    def handle_temp_lbl_type(self, type):
        Data.set_temp_lbl_type(type)
        self.update()

    def handle_temp_set_type(self, type):
        Data.set_temp_set_type(type)
        self.update()

    def handle_temp_set_cool(self):
        Data.set_cool(self.cool)
        self.update()

    def handle_temp_set_heat(self):
        Data.set_heat(self.heat)
        self.update()

    def handle_lock(self):
        if Data.get_door():
            Data.set_locked(not Data.get_locked())
            self.update()

    def handle_in_lights(self, value):
        Data.set_in_lights(value)
        self.update()

    def handle_out_lights(self, value):
        Data.set_out_lights(value)
        self.update()

    def update_temp(self):
        self.lbl_temp.config(text=f"Temperature: {Data.get_temp_str()} {Data.get_temp_lbl_type()}")
        self.lbl_hum.config(text=f"Humidity: {Data.get_hum_str()}")

        if not self.terminate.is_set():
            self.root.after(5000, self.update_temp)

    def on_close(self):
        self.root.destroy()
        self.terminate.set()
        print("tkui terminated")

    def run_ui(self, terminate):
        try:
            self.terminate = terminate
            self.update_temp()
            self.root.mainloop()
        except KeyboardInterrupt:
            self.on_close()