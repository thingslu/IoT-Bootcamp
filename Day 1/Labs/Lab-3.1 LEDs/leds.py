from machine import Pin

# Set the three GPIOs connected to the LEDs to output mode
Red = Pin(21, Pin.OUT)
Green = Pin(22, Pin.OUT)
Blue = Pin(26, Pin.OUT)

# Set the three GPIOs connected to the M5Stack buttons to input mode
A = Pin(39, Pin.IN)
B = Pin(38, Pin.IN)
C = Pin(37, Pin.IN)

while True:
    if A() == 0: # if button A is pressed, turn the Red LED on
        Red(1)
    else:
        Red(0)
    if B() == 0: # if button B is pressed, turn the Green LED on
        Green(1)
    else:
        Green(0)
    if C() == 0: # if button C is pressed, turn the Blue LED on
        Blue(1)
    else:
        Blue(0)