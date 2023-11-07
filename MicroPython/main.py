"""
Created by: Julianne Leblanc-Peltier
Created on: Oct 2023
This module is a Micro:bit MicroPython program which states the distance and uses neopixels
"""

from microbit import *
from hcsr04 import HCSR04
import machine
import neopixel

# variables
sensor = HCSR04(trigger_pin=1, echo_pin=2)
np = neopixel.NeoPixel(machine.Pin(4), 4)
distance = sensor.distance_cm()

# set up
display.show(Image.HAPPY)
np[0] = (0, 0, 0)
np[1] = (0, 0, 0)
np[2] = (0, 0, 0)
np[3] = (0, 0, 0)

while True:
    # if else statement depending on distance
    if button_a.is_pressed():
        print("Distance:", distance, "cm")
        # if distance is greater than or equal to 10, turn neopixels on and state distance in cm
        if distance >= 10:
            np[0] = (0, 255, 0)
            np[1] = (0, 255, 0)
            np[2] = (0, 255, 0)
            np[3] = (0, 255, 0)
            display.show(Image.HAPPY)
        # otherwise turn all neopixels off, and state the distance in cm
        else:
            np[0] = (255, 0, 0)
            np[1] = (255, 0, 0)
            np[2] = (255, 0, 0)
            np[3] = (255, 0, 0)
            display.show(Image.SAD)
    # if button b is pressed, turns all neopixels off and resets.
    if button_b.is_pressed():
        display.clear()
        np[0] = (0, 0, 0)
        np[1] = (0, 0, 0)
        np[2] = (0, 0, 0)
        np[3] = (0, 0, 0)
        display.show(Image.HAPPY)
