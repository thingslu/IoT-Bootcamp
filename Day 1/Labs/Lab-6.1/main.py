print("Entering Main.py")
print("Network connected: {0} , IP: {1}, router: {4}".format(wifisetup.isconnected(), *wifisetup.wlan_sta.ifconfig() ))