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
        #imageFrame = cv2.GaussianBlur(imageFrame, (9, 9), 150)

        # Convert the imageFrame in
        # BGR(RGB color space) to
        # HSV(hue-saturation-value)
        # color space
        blurFrame = cv2.medianBlur(imageFrame,5)
    
        hsvFrame = cv2.cvtColor(blurFrame, cv2.COLOR_BGR2HSV)
        # Defining the range of red color
        lower = np.array([177,85,110])
        upper = np.array([179,255,255])
        
        mask = cv2.inRange(hsvFrame, lower, upper)


        contours, hierarchy = cv2.findContours(mask.copy(),
                                            cv2.RETR_LIST,
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
            if(area > 0):
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
