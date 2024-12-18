Here is your task (I'm having trouble making the picture legible due to the large number of wires...)
You are creating a simulated and very simple home automation system. You will present both a web interface and a tkinter interface that need to cooperate.
You are NOT required to make the web page update itself automatically. I know there is a way to do that, and if you do make it happen you'll get five extra points on the exam grade.
Pin numbers are listed as follows: x (y) where x is the "Board" pin number, that is, simply counting the pins from left to right if you connect your breakout to the board the way we 
have been in class, and y (in parens) is the GPIO pin listed as GPIO nn on the diagrams.
If you don't have one of those little cards, here is a link with the pinouts: https://pinout.xyz/Links to an external site.


You will have one servo to simulate locking and unlocking the door. That servo may be either on the servo board that we used, which will be connected to 3 (2) and 5 (3) as well as voltage 
and ground, and power for the servos themselves, or the PWM will be on pin 11 (17). Only program one of these two into your code. I will have both on my test circuit so I will be able to 
tell which you are using as long as it works correctly.

You will have a button connected to use the built-in PULL-UP resistor connected to pin 7(4) to simulate detecting if the door is open or closed. You may, instead, simply use wires connected 
to the pin and run it to ground or not, because if the switch is closed the door is closed.

The Temperature and Humidity sensor (DHT10 / DHT11) will have its signal / data line connected to 37 (26) almost all the way to the end of the bottom row of pins.

You will have four LEDs - RED, BLUE, GREEN, and WHITE, connected with their anodes at pins 15 (22), 19 (10), 21 (9), and 23 (11), respectively. You will note there is an unused pin between 
the DHT's data line and the RED LED, and an unused pin between the RED LED and the Blue LED. The Green and White use the next pins after the Blue LED.
RED = heat is turned on.
BLUE = AC is turned on.
The green LED represents the interior lights.
The white LED represents the exterior lights.


Your tkinter UI will provide the following functionality:
Temperature and humidity updates every 5 seconds (hint: use a thread), with temperature display in either Fahrenheit or Centigrade based on a UI input element (your choice how to do this).
A place to set heat to: and cool to: temperatures. If the temp goes below the heat to temp, turn on the heat (red LED) until the temperature is back in the acceptable range, if the temp goes 
above the cool to temp, turn on the blue LED to indicate the AC is on until the temperature is back in the acceptable range.
These temperatures must be entered in the current units based on a control in the UI (it may or may not be the same one used to change units for the temperature readout display), and must convert 
to the other units if the user changes the units in the control.
Note: the DHT 10/11 report in centigrade, so your best bet is to store the values that way and simply pass them through a function that will output the value after checking the value of the UI 
element to see which units are to be output.
Your UI will also provide the status of the front door - open or closed (based on the switch) and should only allow you to lock the door (turn the servo 90 degrees) if the door is closed.
Your UI should also provide the status of the exterior and interior lights and allow each to be turned on or off separately. (that is, one control for interior lights and one for the exterior lights).
Your WEB UI must provide the same functionality as the tkinter UI, except that the WEB UI is not REQUIRED to update every 5 seconds. If you can make it do that, you will receive extra 
points as stated above. If not, you can have a button to update.
Your WEB UI must maintain state, so if you turn on the exterior lights, set heat to and cool to temperatures, etc, when you refresh the web page it should report those same values again in 
the interface. (You will need to generate or modify the HTML in your Python program before sending it).
You will submit your python program, commented enough so I know what you're trying to do in case it doesn't work.
Feel free to discuss ideas with your classmates, but I want you to write your own code.
No not actually "start" the quiz until you are ready to submit the code. That's why the instructions are all out here.
