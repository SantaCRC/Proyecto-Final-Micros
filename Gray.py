import cv2
import numpy as np
cam=cv2.VideoCapture(0)
while (1):
    #original image---BGR
    
    frame,img = cam.read()

    ## mask of red color
    mask1 = cv2.inRange(img, (0, 0, 50), (50, 50,255))

    ## mask of blue color
    mask2 = cv2.inRange(img, (50,0,0), (255, 50, 50))

    ## final mask
    mask = cv2.bitwise_or(mask1, mask2)
    target = cv2.bitwise_and(img,img, mask=mask)

    cv2.imshow('Original Image',img)
    cv2.imshow('mask red color',mask1)
    cv2.imshow('mask blue color',mask2)
    cv2.imshow('mask of both colors',mask)
    cv2.imshow('target colors extracted',target)
    cv2.waitKey(0)

cam.release()
cv2.destroyAllWindows()