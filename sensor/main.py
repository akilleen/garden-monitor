import network
from time import sleep
import sensor

sta_if = network.WLAN(network.STA_IF)

# Configure WiFi Here
wifi_ssid = 'PurpleRain' 
wifi_password = 'm34th00k'

sta_if.connect(wifi_ssid, wifi_password)
if sta_if.active():
      print("Wifi connected")
      
      
while True:
  soil_moisture_value = sensor.get_reading()
  print(soil_moisture_value)
  sleep(2)