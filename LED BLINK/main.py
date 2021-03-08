from machine import Pin
import time

#configure the Pin
led = Pin(25, Pin.OUT)


#loop
while True:
#    led.toggle()
    led.on()
    time.sleep_ms(500)  #sleep for 500 ms
    led.off()
    time.sleep(1)  #sleep for 1 second
    print("Hello world!")  #print the data on the console
    
  