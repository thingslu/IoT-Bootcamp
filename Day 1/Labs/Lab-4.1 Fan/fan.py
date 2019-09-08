from machine import Pin, PWM
from time import sleep

# Initializations
A = Pin(39, Pin.IN)
B = Pin(38, Pin.IN)
C = Pin(37, Pin.IN)
pwmFan = PWM(Pin(21), duty=0)
reverseFan = Pin(22, Pin.OUT)

# Duty cycle values must be between 0 and 1023
# We test it inside the loop to keep it 0 - 960 
while True:
    duty = pwmFan.duty()
    if A() == 0:      # if button A is pressed, reverse the fan rotation
        reverseFan(1) 
    else:
        reverseFan(0)
    if B() == 0 and duty < 960: # if button B is pressed, increase the duty cycle
        pwmFan.duty(duty + 64)
    if C() == 0 and duty > 0:   # if button C is pressed, decrease the duty cycle
        pwmFan.duty(duty - 64)
    print("Duty Cycle: ", duty)
    print("Reverse: ", reverseFan())
    sleep(0.1)