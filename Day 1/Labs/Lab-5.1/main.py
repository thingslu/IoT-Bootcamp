from machine import Pin
from neopixel import NeoPixel

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
nf = NeoPixel(Pin(26), 192)

for j in range(1000):
   for i in range(192):
      # For each step of the external loop, "shift" the colors one position
      # The modulus (the remainder of the division) is used to keep the wheel parameter under 256
      nf[i] = wheel( (i+j) % 256 )
   nf.write()

# Turn off
nf.fill((0,0,0))
nf.write()