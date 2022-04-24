import network
from machine import ADC
from time import sleep

sta_if = network.WLAN(network.STA_IF)

# Configure WiFi Here
wifi_ssid = '' 
wifi_password = ''

sta_if.connect(wifi_ssid, wifi_password)
if sta_if.active():
      print("Wifi connected")
      
      
soil_moisture = ADC(0)
while True:
      soil_moisture_value = soil_moisture.read()
      print(soil_moisture_value)
      sleep(2)
