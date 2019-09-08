from machine import Pin
from neopixel import NeoPixel
# Use this for internal M5Stack Neopixels
# np = NeoPixel(15, 10)
# Use this for NeoFlash Neopixels
np = NeoPixel(Pin(26), 192)

count = 0 # to count the number of times the interrupt was triggered

def callback(p):            # This is the function to be executed when the interrupt is triggered
    global count            # Allows the function to modify a varible from the main program
    np[count] = (0,0,128)   # Set Neopixel number 'count - 1' to Blue, 50% brightness
    count = count + 1
    np.write()

PIR = Pin(36, Pin.IN)
PIR.irq(handler=callback, trigger=Pin.IRQ_RISING)