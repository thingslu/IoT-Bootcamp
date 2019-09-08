from machine import SPI, I2C, Pin
from time import sleep
from dht12 import DHT12
from bmp280 import BMP280
from ili934xnew import ILI9341, color565

# M5Stack Pin definitions
TFT_LED_PIN = const(32)
TFT_DC_PIN = const(27)
TFT_CS_PIN = const(14)
TFT_MOSI_PIN = const(23)
TFT_CLK_PIN = const(18)
TFT_RST_PIN = const(33)
TFT_MISO_PIN = const(19)

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)
dht = DHT12(i2c)
bmp = BMP280(i2c)

power = Pin(TFT_LED_PIN, Pin.OUT)
power.value(1)
spi = SPI(2, baudrate=10000000, miso=Pin(TFT_MISO_PIN), mosi=Pin(TFT_MOSI_PIN), sck=Pin(TFT_CLK_PIN))
display = ILI9341(spi, cs=Pin(TFT_CS_PIN), dc=Pin(TFT_DC_PIN), rst=Pin(TFT_RST_PIN))

display.erase()

while True:
    dht.measure()
    sleep(0.5)
    pres = bmp.get()
#   print("Temperature: ",dht.temperature(),"°C")
    txt_temp = "Temperature: " + str(dht.temperature()) + " C "
#   print("Humidity: ",dht.humidity(),"%")
    txt_hum = "Humidity: " + str(dht.humidity()) + " % "
#   print("Temperature BMP280: ", pres[0],"°C")
#   print("Air Pressure: ", pres[1],"Pa")
    txt_pres = "Air Pressure: " + str(pres[1]) + " Pa "
#   print()
#    txt_alt = "Altitude: " + str(44330*(1-(pres[1]/101325)**(1/5.255))) + "  m "
    txt_alt2 = "Altitude: " + str(round(bmp.getAltitude(),1)) + "  m "

    display.set_pos(0,0)
    display.print(txt_temp)
    display.print(txt_hum)
    display.print(txt_pres)
#    display.print(txt_alt)
    display.print(txt_alt2)
    sleep(1.5)

# Clean-up and de initizalize 
# display.erase()
# power(0)