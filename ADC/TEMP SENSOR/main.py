from machine import ADC
import time

adc = ADC(4) #TEMP SENSOR

while True:
    voltage = adc.read_u16() *3.3/65535 #caclulate the ADC voltage
    Temp = 27 - (voltage - 0.706)/0.001721  #convert to temp in C
    
    print(Temp)
    time.sleep(1)  #delay for 1 second

    
    