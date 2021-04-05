from machine import I2C, Pin
import time

i2c = I2C(1, scl=Pin(27), sda=Pin(26), freq=100000);

def pcfLED():
    for x in range(4,8):
        value = 1<<x
        i2c.writeto (39, bytes([value]))
        print(hex(value))
        time.sleep(1)
        

def main():
    for i in range (0, 5):
        pcfLED()
        
        
if __name__ == "__main__":
    main()

