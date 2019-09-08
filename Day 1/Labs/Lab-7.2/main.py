from machine import DAC, I2C, Pin
from vl53l0x import VL53L0X
from math import sin, pi
from time import sleep_us

# initialize i2c and ToF sensor
i2c = I2C(scl=Pin(22), sda=Pin(21))
distance = VL53L0X(i2c)

# instantiate DAC channel
dac = DAC(Pin(25,Pin.OUT))

# create a buffer containing a sine-wave
buf = bytearray(50)
for i in range(len(buf)):
    buf[i] = 128 + int(127 * sin(2 * pi * i / len(buf)))

# function to play a tone
def playtone(delay, repetition, dac, buf):
    for j in range(repetition):
        for i in range(len(buf)):
            dac.write(buf[i])
            sleep_us(delay)

while True:
    dis = distance.read()
    # print("Distance: ", dis, " mm")
    playtone(int(dis/50), 10, dac, buf)