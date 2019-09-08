from machine import SPI, I2C, Pin
from time import sleep
from dht12 import DHT12
from bmp280 import BMP280
from ili934xnew import ILI9341, color565
from openweathermap import getforecast, getcurrentweather
import tt14, tt24, tt32

# List of city ID city.list.json.gz can be downloaded here
# http://bulk.openweathermap.org/sample/
CityID='2960316'

#APIKey='Put YOUR API KEY here'

# M5Stack Pin definitions
TFT_LED_PIN = const(32)
TFT_DC_PIN = const(27)
TFT_CS_PIN = const(14)
TFT_MOSI_PIN = const(23)
TFT_CLK_PIN = const(18)
TFT_RST_PIN = const(33)
TFT_MISO_PIN = const(19)

# Initialize ENV. module
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)
dht = DHT12(i2c)
bmp = BMP280(i2c)

# Initialize the display
power = Pin(TFT_LED_PIN, Pin.OUT)
power.value(1)
spi = SPI(2, baudrate=10000000, miso=Pin(TFT_MISO_PIN), mosi=Pin(TFT_MOSI_PIN), sck=Pin(TFT_CLK_PIN))
display = ILI9341(spi, cs=Pin(TFT_CS_PIN), dc=Pin(TFT_DC_PIN), rst=Pin(TFT_RST_PIN))

display.erase()
display.set_font(tt24)

print("\nGeting current weather")
country,city,temp, temp_min, temp_max, short_weather, long_weather = getcurrentweather(CityID, APIKey)
# print("Current weather for {}, {}: {}°C, {}".format(city, country, temp, long_weather))
txt_location = "{}, {}".format(city, country)
txt_weather = "Current weather {}".format(long_weather)
txt_temp = "{} C".format(temp)
txt_min = "Lo {} C".format(temp_min)
txt_max = "Hi {} C".format(temp_max)
# print("min {}, max {} ".format(temp_min, temp_max))

display.print(txt_location)
display.print(txt_weather)

display.set_pos(50,60)
display.set_font(tt32)
display.print(txt_temp)

display.set_pos(200,60)
display.set_font(tt14)
display.print(txt_min)
display.print(txt_max)

print('\nRetrieving the weather forecast')
country, city, short_forecast, long_forecast, temp, humidity = getforecast(CityID, APIKey)
# print("Tomorrow's forecast: {}, {}°C - {}% humidity\n".format(long_forecast, temp, humidity))
txt_forecast = "Tomorrow: {}, {} C".format(long_forecast, temp)

display.set_pos(0,100)
display.set_font(tt24)
display.print(txt_forecast)

sleep(2)
display.set_pos(20,160)
display.set_font(tt14)
display.print("Inside sensor temperature and humidity")

display.set_pos(120,180)
display.set_font(tt24)

while True:
    dht.measure()
    sleep(0.5)
    pres = bmp.get()
#   print("Temperature: ",dht.temperature(),"°C")
#   print("Humidity: ",dht.humidity(),"%")
    txt_inside = str(dht.temperature()) + " C - " + str(dht.humidity()) + " % "
#   print("Temperature BMP280: ", pres[0],"°C")
#   print("Air Pressure: ", pres[1],"Pa")
#   print()
#   txt_alt = "Altitude: " + str(44330*(1-(pres[1]/101325)**(1/5.255))) + "  m "

    display.print(txt_inside)
    sleep(1.5)
    display.set_pos(120,180)

# Clean-up and de initizalize 
# display.erase()
# power(0)
