# Demo 5.1 - Neopixels
import machine, neopixel
np = neopixel.NeoPixel(machine.Pin(26), 10)
np[8] = (128,0,0)   # Red - 50% brightness
np.write()

np[8] = (0,0, 255)   # Blue - 100% brightness
np.write()

np[8] = (128,128,0)  # Yellow - 50% bright
np.write()

np[4] = (0,128,128)  # Cyan - 50% bright
np.write()

# Turn off
np.fill((0,0,0))
np.write()

def wheel(pos):
   # Input a value 0 to 255 to get a color value.
   # The colors goes from Red - Green - Blue, back to Red.
   # Brightness is kept at 33% of maximum.
   if pos < 0 or pos > 255:
      return (0, 0, 0)
   if pos < 85:
      return (85 - pos, pos, 0)
   if pos < 170:
      pos = pos - 85
      return (0, 85 - pos, pos)
   pos = pos - 170
   return (pos, 0, 85 - pos)

# Raimbow
from machine import Pin
from neopixel import NeoPixel
nf = NeoPixel(Pin(26), 192)

for i in range(192):
   nf[i] = wheel(i)
nf.write()

# Turn off
nf.fill((0,0,0))
nf.write()

# Demo 5.3 - PIR
from machine import Pin
from time import sleep

PIR = Pin(36, Pin.IN)
while True:
    if PIR.value():
        print('Movement detected !')
    else:
        print('Everything quiet...')
    sleep(1)   

# Demo 5.4 - External interrupts
from machine import Pin
def callback(p):                  # This is the function to be executed 
    print('Something moved', p)   # when the event happens

PIR = Pin(36, Pin.IN)
# The parameters handler and trigger defines the event
PIR.irq(handler=callback, trigger=Pin.IRQ_RISING)

# Demo 5.5 - External interrupts Global Variable(s)
from machine import Pin
count = 0    # the number of times the interrupt was been triggered
def callback(p):              # This is the function to be executed 
    global count              # Allows the function to modify a 
    count = count + 1         # variable from the main program
    print('Something moved {} times'.format(count))

PIR = Pin(36, Pin.IN)
# The parameters handler and trigger defines the event
PIR.irq(handler=callback, trigger=Pin.IRQ_RISING)