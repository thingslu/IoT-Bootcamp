# This file is executed on every boot (including wake-boot from deepsleep)
import sys
import network

# Set default path
# Needed for importing modules
sys.path.append('flash/lib')

# Auto Connect to the network, starts autoconfig if needed
import wifisetup
wifisetup.auto_connect()