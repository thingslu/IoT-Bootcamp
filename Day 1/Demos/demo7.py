# Demo 7.1 - I²C bus
from machine import I2C, Pin
i2c = I2C(sda=Pin(21), scl=Pin(22))
i2c.scan()

# Connect the ENV and TOF sensors
i2c.scan()

# Demo 7.2 - ENV module
from machine import I2C, Pin
from time import sleep
from dht12 import DHT12
from bmp280 import BMP280

i2c = I2C(scl=Pin(22), sda=Pin(21))
dht = DHT12(i2c)
bmp = BMP280(i2c)

while True:
    dht.measure()
    sleep(0.5)
    pres = bmp.get()
    print("Temperature: ",dht.temperature(),"°C")
    print("Humidity: ",dht.humidity(),"%")
#    print("Temperature BMP280: ", pres[0],"°C")
    print("Air Pressure: ", pres[1],"Pa")
    print()
    sleep(0.5)

# it does not work...
# try first loading the two libraries bmp280.py and dht12.py
from machine import I2C, Pin
from time import sleep
from dht12 import DHT12
from bmp280 import BMP280

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)
dht = DHT12(i2c)
bmp = BMP280(i2c)

while True:
    dht.measure()
    sleep(0.5)
    pres = bmp.get()
    print("Temperature: ",dht.temperature(),"°C")
    print("Humidity: ",dht.humidity(),"%")
#    print("Temperature BMP280: ", pres[0],"°C")
    print("Air Pressure: ", pres[1],"Pa")
    print()
    sleep(0.5)

# Demo 7.3 - Display
from ili934xnew import ILI9341, color565
from machine import Pin, SPI

# M5Stack Pin definitions
TFT_LED_PIN = const(32)
TFT_DC_PIN = const(27)
TFT_CS_PIN = const(14)
TFT_MOSI_PIN = const(23)
TFT_CLK_PIN = const(18)
TFT_RST_PIN = const(33)
TFT_MISO_PIN = const(19)

# The Zen of MicroPython by Nicholas H. Tollervey
text = 'Code,\nHack it,\nLess is more,\nKeep it simple,\nSmall is beautiful,\n\nBe brave! Break things! Learn and have fun!\nExpress yourself with MicroPython.\n\nHappy hacking ! :-)' 

power = Pin(TFT_LED_PIN, Pin.OUT)
power.value(1)

spi = SPI(2, baudrate=40000000, miso=Pin(TFT_MISO_PIN), mosi=Pin(TFT_MOSI_PIN), sck=Pin(TFT_CLK_PIN))
display = ILI9341(spi, cs=Pin(TFT_CS_PIN), dc=Pin(TFT_DC_PIN), rst=Pin(TFT_RST_PIN))

display.erase()
display.set_pos(0,0)
display.print(text)

# Clean-up and de initizalize 
# display.erase()
# power(0)


# Demo 7.4 - ToF module
from machine import I2C, Pin
from vl53l0x import VL53L0X

# initialize i2c and ToF sensor
i2c = I2C(scl=Pin(22), sda=Pin(21))
distance = VL53L0X(i2c)

while True:
    dis = distance.read()
    print("Distance: ", dis, " mm")

# Demo 7.5 - Playing tones on the speaker
from machine import DAC, Pin
from math import sin, pi
from time import sleep_us

dac = DAC(Pin(25,Pin.OUT))

# create a buffer containing a sine-wave
buf = bytearray(50)
for i in range(len(buf)):
    buf[i] = 128 + int(127 * sin(2 * pi * i / len(buf)))
 
while True:
    for i in range(len(buf)):
        dac.write(buf[i])
        sleep_us(1)

# Demo 7.6 - Playing tones on the speaker now with a function
from machine import DAC, Pin
from math import sin, pi
from time import sleep_us

dac = DAC(Pin(25,Pin.OUT))
# create a buffer containing a sine-wave
buf = bytearray(50)
for i in range(len(buf)):
    buf[i] = 128 + int(127 * sin(2 * pi * i / len(buf)))

def playtone(delay, repetition, dac, buf):
    for j in range(repetition):
        for i in range(len(buf)):
            dac.write(buf[i])
            sleep_us(delay)

playtone(1, 100, dac, buf)
playtone(5, 100, dac, buf)
playtone(10, 100, dac, buf)
playtone(50, 100, dac, buf)
playtone(70, 100, dac, buf)
playtone(85, 100, dac, buf)
playtone(100, 100, dac, buf)