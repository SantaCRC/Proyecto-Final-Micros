import cv2
import numpy as np
cam=cv2.VideoCapture(0)
while (1):
    #original image---BGR
    
    ret,img=cam.read()
    cv2.imshow('Output',img)
    #gray image
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayscale',img1)
    #threshholded image
    img2=cv2.inRange(img,cv2.cv.Scalar(3,3,130),cv2.cv.Scalar(50,50,255))
    cv2.imshow('threshoalded',img2)


    key=cv2.waitKey(200)
    if key==32:
        break

cam.release()
cv2.destroyAllWindows()