from microbit import *
import radio

uart.init(baudrate=115200)

radio.on()
while True:
    if uart.any() == True:
        msg = uart.readline()
        #display.scroll(msg)
        radio.send(msg)

    i = 0
    try:
        msg2 = radio.receive()
        if msg2 != None:
            i+=1 
            if i == 1:
                i=0
                print(msg2)
                display.show(Image.HAPPY)
        else:
            display.show(Image.SAD)
    except:
        display.clear()
        