from microbit import *
import radio

def forward(n):
    display.show(Image.HAPPY)
    pin0.write_analog(511)
    pin8.write_digital(0) 
    pin1.write_analog(511)
    pin12.write_digital(0)
    sleep(n)
    
def backward(n):
    display.show(Image.SAD)
    pin0.write_analog(511)
    pin8.write_digital(1) 
    pin1.write_analog(511)
    pin12.write_digital(1)
    sleep(n)
    
def turnR(n):
    display.show(Image.ARROW_E)
    pin0.write_analog(511)
    pin8.write_digital(0) 
    pin1.write_analog(511)
    pin12.write_digital(1)
    sleep(n)
    
def turnL(n):
    display.show(Image.ARROW_W)
    pin0.write_analog(511)
    pin8.write_digital(1) 
    pin1.write_analog(511)
    pin12.write_digital(0)
    sleep(n)

radio.on()

while True:
    lastTurn = 'l'
    sleft = pin11.read_digital()
    sright = pin5.read_digital()
    #display.scroll(str([sleft,sright]))
    radio.send(str([sleft,sright]))
    try:
        msg = radio.receive()
        for i in range(len(msg)):
            try:
                if int(msg[i])/1 == int(msg[i]):
                    pass
            except:
                if i!=0:
                    msg = msg[:i+1]
                
    except:
        pass
    try:
        if msg == None:
            pass
        elif msg[0] == 'f':
            forward(int(msg[1:]))
        elif msg[0] == 'b':
            if lastTurn == 'l':
                turnR(int(msg[1:])*3)
            else:
                turnL(int(msg[1:])*3)
            forward(int(msg[1:])*6)
        elif msg[0] == 'r':
            lastTurn = 'r'
            turnR(int(msg[1:]))
            forward(int(msg[1:])*3)
        elif msg[0] == 'l':
            lastTurn = 'l'
            turnL(int(msg[1:]))
            forward(int(msg[1:])*3)
    except:
        pass
        
    if msg != None:
        display.clear()
        pin0.write_analog(0)
        pin8.write_digital(0)
        pin1.write_analog(0)
        pin12.write_digital(0)