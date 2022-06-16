# Python code for Multiple Color Detection


from cv2 import line
import numpy as np
import threading
import cv2
import queue

import Archivo
x_queue = queue.Queue()
y_queue = queue.Queue()
linea = []
#from smbus import SMBus
#addr = 0x8 # bus address
#bus = SMBus(1) # indicates /dev/ic2-1




def archivo(line):
    f = open ('holamundo.txt','a')
    f.write(line)
    f.close()


def main(red_lower, red_upper):
    # Capturing video through webcam
    webcam = cv2.VideoCapture(0)
    webcam.set(3,640)
    webcam.set(4,480)
    estado = "Sin objeto"

    # Start a while loop
    while(1):

        # Reading the video from the
        # webcam in image frames
        _, imageFrame = webcam.read()
        imageFrame = cv.GaussianBlur(imageFrame, (9, 9), 150)

        # Convert the imageFrame in
        # BGR(RGB color space) to
        # HSV(hue-saturation-value)
        # color space
        hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

        # Set range for red color and
        # define mask
        #red_lower = np.array([136, 87, 111], np.uint8)
        #red_upper = np.array([180, 255, 255], np.uint8)
        lower_red = np.array([0, 100, 20])
        upper_red = np.array([10, 255, 255])
        mask0 = cv2.inRange(hsvFrame, lower_red, upper_red)

        # upper mask (170-180)
        lower_red = np.array([160,100,20])
        upper_red = np.array([179,255,255])
        mask1 = cv2.inRange(hsvFrame, lower_red, upper_red)
 
        full_mask = mask0 + mask1
        kernel = np.ones((7,7),np.uint8)
# Remove unnecessary noise from mask
        mask = cv2.morphologyEx(full_mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        contours, hierarchy = cv2.findContours(mask.copy(),
                                            cv2.RETR_EXTERNAL,
                                            cv2.CHAIN_APPROX_SIMPLE)
        
        #cv2.circle(imageFrame, (320, 240), 25, (0, 0, 255), 2)
        if estado == "siguiendo":
            estado = "perdido"
        try:
            x_mark=0
        except:
            pass
        for pic, contour in enumerate(contours):
            x_mark=1
            area = cv2.contourArea(contour)
            if(area > 250):
                estado = "siguiendo"
                x, y, w, h = cv2.boundingRect(contour)
                imageFrame = cv2.rectangle(imageFrame, (x, y),
                                        (x + w, y + h),
                                        (0, 0, 255), 2)
                linea.append([int(x+w/2),int(y+h/2)])
                
                if len(linea)>50:
                    linea.pop(0)

                cv2.putText(imageFrame, "Rojo", (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                            (0, 0, 255))
                cv2.putText(imageFrame, "Coordenada: x:{} y:{} ".format(x,y),(30,30),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))
                
                x_queue.put(x)
                #bus.write_byte(addr,x)
                #y_queue.put(y)
                threading.Thread(target=Archivo.guardar_linea,args=(x_queue,)).start()
                

                for i in range(len(linea)-2):
                    cv2.line(imageFrame, (linea[i][0],linea[i][1]), (linea[i+1][0],linea[i+1][1]), (0, 0, 255), 2)
            else:
                estado = "perdido"
            if x_mark>0:
                break

        cv2.putText(imageFrame, "Estado : {}".format(estado), (10, 450),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))
        cv2.imshow("Proyecto final", imageFrame)
        #cv2.imshow("Proyecto final", red_mask)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            break

#t=threading.Thread(target=Archivo.guardar_linea,args=("hola\n",))
    #t.start()
