from telemetrix import telemetrix
import threading
import time
SERVO_PIN = 9
SERVO_PIN1 = 10
board = telemetrix.Telemetrix()
board.set_pin_mode_servo(SERVO_PIN, 100, 3000)
board.set_pin_mode_servo(SERVO_PIN1, 100, 3000)
last_x=0
last_y=0
board.servo_write(SERVO_PIN1, 90)


def enX(x):
    print("x:",x)
    if  x<200:
        try:
            x=45
            board.servo_write(SERVO_PIN1, x)
        except Exception as e:
            print("Error: no se puede mover " + str(e))
            board.servo_write(SERVO_PIN1, 90)
    elif x>400:
        try:
            x=135
            board.servo_write(SERVO_PIN1, x)
        except Exception as e:
            print("Error: no se puede mover" + str(e))
            board.servo_write(SERVO_PIN1, 90)
    time.sleep(0.05)
    board.servo_write(SERVO_PIN1, 90)
    

def main(posicion):
    x=posicion[0]
    y=posicion[1]
    last_x=round(x*0.28)
    last_y=round(y*0.28)
    threading.Thread(target=enX, args=(x,)).start()
    if y>240:
        try:
            y=last_y+10
            board.servo_write(SERVO_PIN, y)
        except Exception as e:
            print("Error: no se puede mover" + str(e))
    elif y<240:
        try:
            y=last_y-10
            board.servo_write(SERVO_PIN, y)
        except Exception as e:
            print("Error: no se puede mover" + str(e))
    last_x=x
    last_y=y

if __name__ == '__main__': 
    #main([0,0])
    main([0,100])
    main([90,200])