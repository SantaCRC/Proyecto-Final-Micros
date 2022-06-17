# import the opencv library
import cv2
import time
from telemetrix import telemetrix
import threading
SERVO_PIN1 = 9
SERVO_PIN2 = 10
from servos1 import board
board.set_pin_mode_servo(SERVO_PIN2, 100, 3000)
board.set_pin_mode_servo(SERVO_PIN1, 100, 3000)
ejeX=90
ejeY=90
CB_PIN_MODE = 0
CB_PIN = 1
CB_VALUE = 2
CB_TIME = 3
CA_VALUE = 2

def the_callbackX(data):
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data[CB_TIME]))
    #print(f'Pin Mode: {data[CB_PIN_MODE]} Pin: {data[CB_PIN]} Value: {data[CB_VALUE]} Time Stamp: {date}')
    valorX=data[CB_VALUE]
    valorX=round(valorX*0.20)
    board.servo_write(SERVO_PIN1, valorX)
 
def the_callbackY(datos):
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(datos[CB_TIME]))
    valorY=datos[CA_VALUE]
    print(f'Pin Mode: {datos[CB_PIN_MODE]} Pin: {datos[CB_PIN]} Value: {datos[CA_VALUE]} Time Stamp: {date}')
    if valorY>600 and valorY<900:
        board.servo_write(SERVO_PIN2, 90)
    elif valorY<400:
        board.servo_write(SERVO_PIN2, 180)
    elif valorY<700 and valorY>500:
        board.servo_write(SERVO_PIN2, 0)
    time.sleep(0.1)
    board.servo_write(SERVO_PIN2, 90)

def leer():
    board.set_pin_mode_analog_input(5,5,the_callbackY)
    board.set_pin_mode_analog_input(4,5,the_callbackX)
    

timer = int(120)
def main():
    leer()
    board.servo_write(SERVO_PIN1, 90)
    board.servo_write(SERVO_PIN2, 90)
    timer = int(120)
    # define a video capture object
    vid = cv2.VideoCapture(0)
    prev = time.time()
    while(True):
        
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        cv2.circle(frame, (320,240), 75, (255, 255, 255), 2)
        cv2.putText(frame, str(timer), (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        cur = time.time()
        
        if cur - prev >=1:
            prev=cur
            timer -= 1
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    board.shutdown()
    # Destroy all the windows
    cv2.destroyAllWindows()
