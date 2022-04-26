import network
from time import sleep
import sensor
import publish
import packages

packages.install()
sta_if = network.WLAN(network.STA_IF)

# Configure WiFi Here
wifi_ssid = '' 
wifi_password = ''

sta_if.connect(wifi_ssid, wifi_password)
if sta_if.active():
      print("Wifi connected")
      
      
while True:
  soil_moisture_value = sensor.get_reading()
  publish.publish(soil_moisture_value)
  sleep(10)