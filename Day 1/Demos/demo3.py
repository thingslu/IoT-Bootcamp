# Demo 3.1 - GPIOs and the machine module
import machine
BlueLED = machine.Pin(26, machine.Pin.OUT)

# turning the Blue LED on and off

BlueLED.value(1)

# pause

BlueLED.value(0)

# Blinking the Blue LED

while True:
     BlueLED.value(1)
     BlueLED.value(0)

# Blinking the Blue LED slowly

import time
while True:
     BlueLED.value(1)
     time.sleep(0.5)
     BlueLED.value(0)
     time.sleep(0.5)

# Now with three LEDs

import machine
Red = machine.Pin(21, machine.Pin.OUT)
Green = machine.Pin(22, machine.Pin.OUT)
Blue = machine.Pin(26, machine.Pin.OUT)

Red.value(1)
# pause
Red(0)
# pause
Blue(1)
# pause
Blue(0)
# pause
Green(1)
# pause
Green(0)

# Demo 3.2 – Using input
from machine import Pin
A = Pin(39, Pin.IN)
# pause
A.value()
# Press the first button and run it again

# Demo 3.2 – If statement
if A.value() == 0:
    print("Do sommething")

# Pause

while True:
    if A.value() == 0:
        print("Do sommething")
    else:
        print("Do something else")
        
# First program

from machine import Pin
Blue = Pin(26, Pin.OUT)
A = Pin(39, Pin.IN)

while True:
    if A.value() == 0:
        Blue(1)
    else:
        Blue(0)