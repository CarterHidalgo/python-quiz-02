# Name: Carter Hidalgo
# Class: Pi and Python
# File: main.py

import threading, time
from tkinter import *
from queue import Queue

def cleanup():
    print("gpio cleanup")
    # GPIO.cleanup()

def setup_ui():
    def update():
        print(f"temp_type: {temp_type.get()}")

        root.after(1000, update)

    def on_close():
        root.destroy()
        print("closing ui")
        
    root = Tk()

    temp_type = StringVar(value="F")

    root.geometry("400x300")
    root.title("Quiz 02 UI")

    rb_far = Radiobutton(root, text="Farenheit", variable=temp_type, value="F")
    rb_far.pack(anchor=W)
    rb_cel = Radiobutton(root, text="Celcius", variable=temp_type, value="C")
    rb_cel.pack(anchor=W)

    update()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

def main():

    setup_ui()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()