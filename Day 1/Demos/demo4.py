# Demo 4.1 - Blinky PWM version
from machine import Pin, PWM
BlueLED = PWM(Pin(26), freq=1, duty=512)

# pause
BlueLED.freq(10)
BlueLED.freq(30)
BlueLED.freq(60)

# pause
BlueLED.duty(300)
BlueLED.duty(100)
BlueLED.duty(700)

# pause
BlueLED.deinit()

# Demo 4.2 - Fading LEDs
from machine import Pin, PWM
from time import sleep
BlueLED = PWM(Pin(26), freq=5000, duty=0)
while True:
    for i in range(1024):
       BlueLED.duty(i)
       sleep(0.001)
    for i in range(1024, 0, -1):
       BlueLED.duty(i)
       sleep(0.001)

# pause
BlueLED.deinit()

# Demo 4.3 - Multicolor LED
from machine import Pin, PWM

RedLED = PWM(Pin(21), duty=0)
GreenLED = PWM(Pin(22), duty=0)
BlueLED = PWM(Pin(26), duty=0)

RedLED.duty(round(1024*1/5))
GreenLED.duty(round(1024*3/5))
BlueLED.duty(round(1024*4/5))

# pause
RedLED.deinit()
GreenLED.deinit()
BlueLED.deinit()

# Demo 4.4 - Rainbow
from machine import Pin, PWM
from time import sleep

def fade(led, begin=0, end=1024, step=1):
    for i in range(begin, end, step):
        led.duty(i)
        sleep(0.001)

RedLED = PWM(Pin(21), duty=0)
GreenLED = PWM(Pin(22), duty=0)
BlueLED = PWM(Pin(26), duty=0)

while True:
   fade(GreenLED)                           # Ramp up green
   fade(RedLED, begin=1024,end=0,step=-1)   # Ramp down red
   fade(BlueLED)                            # Ramp up blue
   fade(GreenLED, begin=1024,end=0,step=-1) # Ramp down green
   fade(RedLED)                             # Ramp up red
   fade(BlueLED, begin=1024,end=0,step=-1)  # Ramp down blue

# Demo 4.5 - cross fading Rainbow
from machine import Pin, PWM
from time import sleep

def crossFade(ledUp, ledDown, begin=0, end=1024):
   for i in range(begin, end):
      ledUp.duty(i)
      ledDown.duty(1023-i)
      sleep(0.002)

RedLED = PWM(Pin(21), duty=0)
GreenLED = PWM(Pin(22), duty=0)
BlueLED = PWM(Pin(26), duty=0)

while True:
   crossFade(GreenLED, RedLED)    # Ramp up green / ramp down red
   crossFade(BlueLED, GreenLED)   # Ramp up red / ramp down green
   crossFade(RedLED, BlueLED)     # Ramp up red / ramp down blue

# Demo 4.6 - L9110 Fan Motor Module
from machine import Pin
inA = Pin(21, Pin.OUT)
inB = Pin(22, Pin.OUT)

# pause

inA.value(0)    
inB.value(1)    # Forward
# pause
inB.value(0)    # Stop
# pause
inA.value(1)    # Reverse

# Demo 4.7 - L9110 Fan Motor Module with PWM
from machine import Pin, PWM
pwmFan = PWM(Pin(21))
reverseFan = Pin(22, Pin.OUT)

pwmFan.duty(717) # 70% duty cycle ( 70 * 1024 / 100 )
# pause
pwmFan.duty(307) # 30% duty cycle ( 30 * 1024 / 100 )
# pause
reverseFan.value(1)

# Demo 4.8 - SG90 MicroServo
from machine import Pin, PWM

# Set the frequency to 50Hz (one cycle per 20ms)
pwmServo = PWM(Pin(26), freq=50, duty=8)

pwmServo.duty(34)  # 20ms *  34 / 1024 = 0.66 ms)
pwmServo.duty(77)  # 20ms *  77 / 1024 = 1.50 ms)
pwmServo.duty(132) # 20ms * 132 / 1024 = 2.58 ms)