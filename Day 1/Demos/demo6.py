# Demo 6.1 - Connect to WiFI Client
# TURN THE WiFi ROUTER ON!!!
#
import network, time
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('IOTBOOTCAMP', 'MicroPython')

Try = 50
while not wlan.isconnected():
    time.sleep(0.1)
    Try = Try - 1
    print('.', end='')
    if Try == 0:
        wlan.active(False)
        break

if wlan.isconnected():
    print("===== Station Connected to WiFi =====\n")
else:
    print("!!!!! Not able to connect to WiFi !!!!!")

config = wlan.ifconfig()
print("IP Address, Subnet Mask, Default Gateway, DNS")
print(config)

# Demo 6.2 - Set time  & Network Time 
from machine import RTC
import ntptime 
rtc = RTC() # initializes internal Real Time Clock
rtc.datetime()
try:
    ntptime.settime() # Get time and date from NTP server and update internal RTC
    print("Year, Month, Day, Day of the Weak, Hour, Minutes, Seconds, Sub seconds")
    rtc.datetime()
except:
    print('ERROR: Cannot set time via NTP')

# Demo 6.3 - Connect as a WiFI Access Point (Router)
import network, time
ap = network.WLAN(network.AP_IF)
ap.active(True)

mode = ["open", "WEP", "WPA-PSK", "WPA2-PSK", "WPA/WPA2-PSK"]

print("\n===== Access point started =====\n")
print("This ESP32 Access point is")
print("Network SSID {}, Channel {}, Security: {}, {}".format(
    ap.config('essid'),
    ap.config('channel'),
#    ap.config('dhcp_hostname'),
#    ap.config('mac'),
    mode[ap.config('authmode')],
    'Hidden' if ap.config('hidden') else 'Visible'
))
print("\nIP Address, Subnet Mask, Default Gateway, DNS")
print(ap.ifconfig())

# Demo 6.4 - Scan for WiFi Access Points 
# CODE STILL NEEDS TO BE FIXED
import network
wlan = network.WLAN(network.STA_IF)
_ = wlan.active(True)

_networks = wlan.scan(True)
_networks = sorted(_networks, key=lambda x: x[3], reverse=True)
_f = "{0:<32} {2:>8} {3:>8} {5:12} {6:>8}"
print(_f.format("SSID",'mac',"Channel","Signal","0","Authmode","Hidden"))
for row in _networks:
    print(_f.format(*row))