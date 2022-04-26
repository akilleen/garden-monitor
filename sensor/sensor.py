from machine import ADC

def get_reading():
    soil_moisture = ADC(0)
    soil_moisture_value = soil_moisture.read()
    return soil_moisture_value
