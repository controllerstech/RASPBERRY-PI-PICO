from machine import ADC 
import time

adc = ADC(0)  #ADC0 at pin 26
ADC_VREF = 3.3

while True:
    voltage = adc.read_u16() * ADC_VREF / 65535  #get the ADC voltage
    angle = voltage*300 / 3.3  #Convert to the angle 0-300
    print (angle)
    time.sleep_ms (5)  #sleep for 5ms