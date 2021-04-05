import i2clcd

def main():
    i2clcd.init()
    i2clcd.clear()
    i2clcd.goto(0,1)
    i2clcd.string("hello world")
    i2clcd.goto(1,1)
    i2clcd.string('from PI PICO')
    
    value = 12345
    flot = 123.45
    
    i2clcd.clear()
    i2clcd.goto(0,1)
    i2clcd.string(str(value))
    i2clcd.goto(1,1)
    i2clcd.string(str(flot))
    
    
    
    
if __name__ == "__main__":
    main()
