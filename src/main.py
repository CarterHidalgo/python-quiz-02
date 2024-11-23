# Name: main.py
# Author: Carter Hidalgo
#
# Purpose: Start logic, web, and tkui threads

# NOTES
# Run the program from main.py. Interact with the circuit using the tkui and webui. Know that there are still many edge cases,
# and the program is not fully thread safe, although the speed at which data updates has not been a problem during testing.
# There is mild user input validation (cool-heat range must always have int or float and cool may not equal or be higher than
# heat) but "impossible" temps such as -1000000 C are still allowed. To close the program safely close the tkui by clicking the
# X. This will cleanup GPIO and stop the circuit, but the web server will continue running due to keyboard interrupts not 
# registering and (apparently) being the go-to method of stopping servers. After "tkui terminated" and "circuit terminated" output
# it is safe to completely terminate the program by closing the terminal. 

# Instructions were slightly unclear, but pushing the button opens the door provided it is unlocked and releasing it closes the
# door. The door may only be locked if the door is closed (default state)

# Servo is controlled using PWM without a servo board. 5V + GND + 1 GPIO pin connected direction to the servo 3-wire (a micro servo 9g)

# Program contains light commenting, but most code is named to be self-commenting. Comments added at vital parts of the program

import threading
from web import WebUI
from circuit import Circuit
from tkui import TKUI

def main():
    terminate = threading.Event()

    ui = TKUI()

    circuit_thread = threading.Thread(target=Circuit.run, args=(ui, terminate,))
    circuit_thread.start()

    web_ui_thread = threading.Thread(target=WebUI.run, args=(ui,))
    web_ui_thread.start()

    ui.run_ui(terminate)

if __name__ == '__main__':
    main()
