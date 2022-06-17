import pyfirmata
import threading
import time
board = pyfirmata.Arduino('/dev/ttyACM0')
iter8 = pyfirmata.util.Iterator(board)
iter8.start()
pin9 = board.get_pin('d:9:s')
pin10 = board.get_pin('d:10:s')
last_x=0
last_y=0
pin9.write(90)


def enX(x):
    print("x:",x)
    if  x<200:
        try:
            x=45
            pin9.write(x)
        except :
            print("Error: no se puede mover")
            pin9.write(90)
    elif x>400:
        try:
            x=135
            pin9.write(x)
        except:
            print("Error: no se puede mover")
            pin9.write(90)
    time.sleep(0.05)
    pin9.write(90)
    

def main(posicion):
    x=posicion[0]
    y=posicion[1]
    last_x=x*0.28
    last_y=y*0.28
    threading.Thread(target=enX, args=(x,)).start()
    if y>240:
        try:
            y=last_y+10
            pin10.write(y)
        except :
            print("Error: no se puede mover")
    elif y<240:
        try:
            y=last_y-10
            pin10.write(y)
        except:
            print("Error: no se puede mover")
    last_x=x
    last_y=y

if __name__ == '__main__': 
    main([90,0])
    main([90,200])