import cv2
import numpy as np
import sys

image_hsv = None
pixel = (0,0,0) #RANDOM DEFAULT VALUE


def check_boundaries(value, tolerance, ranges, upper_or_lower):
    if ranges == 0:
        # set the boundary for hue
        boundary = 180
    elif ranges == 1:
        # set the boundary for saturation and value
        boundary = 255

    if(value + tolerance > boundary):
        value = boundary
    elif (value - tolerance < 0):
        value = 0
    else:
        if upper_or_lower == 1:
            value = value + tolerance
        else:
            value = value - tolerance
    return value

def pick_color(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = image_hsv[y,x]

        #HUE, SATURATION, AND VALUE (BRIGHTNESS) RANGES. TOLERANCE COULD BE ADJUSTED.
        # Set range = 0 for hue and range = 1 for saturation and brightness
        # set upper_or_lower = 1 for upper and upper_or_lower = 0 for lower
        hue_upper = check_boundaries(pixel[0], 50, 0, 1)
        hue_lower = check_boundaries(pixel[0], 50, 0, 0)
        saturation_upper = check_boundaries(pixel[1], 50, 1, 1)
        saturation_lower = check_boundaries(pixel[1], 50, 1, 0)
        value_upper = check_boundaries(pixel[2], 50, 1, 1)
        value_lower = check_boundaries(pixel[2], 50, 1, 0)

        upper =  np.array([hue_upper, saturation_upper, value_upper])
        lower =  np.array([hue_lower, saturation_lower, value_lower])
        print(lower, upper)

        #A MONOCHROME MASK FOR GETTING A BETTER VISION OVER THE COLORS 
        image_mask = cv2.inRange(image_hsv,lower,upper)
        cv2.imshow("Mask",image_mask)



def main():

    global image_hsv, pixel

    #OPEN DIALOG FOR READING THE IMAGE FILE
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cv2.imshow("BGR",frame)

    #CREATE THE HSV FROM THE BGR IMAGE
    image_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV",image_hsv)

    #CALLBACK FUNCTION
    cv2.setMouseCallback("HSV", pick_color)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



def init():
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        marco=cv2.imshow("Calibracion", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            cam.release()
            cv2.destroyAllWindows()
            main()

if __name__=='__main__':
    init()