import numpy as np
import cv2
from resizeFunc import *


def nothing(x):
    pass

cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars', 600,250)
cv2.createTrackbar('Hue_min', 'Trackbars',0,180,nothing)
cv2.createTrackbar('Hue_max', 'Trackbars',180,180,nothing)
cv2.createTrackbar('Sat_min', 'Trackbars',0,255,nothing)
cv2.createTrackbar('Sat_max', 'Trackbars',255,255,nothing)
cv2.createTrackbar('Val_min', 'Trackbars',0,255,nothing)
cv2.createTrackbar('Val_max', 'Trackbars',255,255,nothing)


# hsv = cv2.cvtColor(image, cv2.COLORBGR2HSV)



while True:
    # Read an image, a window and bind the function to window
    image = resize_img("image.jpg", 10)

#defining a kernel
    k_sharped = np.array([[0,-1,0],
                     [-1,5,-1],
                     [0,-1,0]])


    sharpened = cv2.filter2D(image, -1, k_sharped)




    hmin = cv2.getTrackbarPos('Hue_min', 'Trackbars')
    hmax = cv2.getTrackbarPos('Hue_max', 'Trackbars')
    smin = cv2.getTrackbarPos('Sat_min', 'Trackbars')
    smax = cv2.getTrackbarPos('Sat_max', 'Trackbars')
    vmin = cv2.getTrackbarPos('Val_min', 'Trackbars')
    vmax = cv2.getTrackbarPos('Val_max', 'Trackbars')

    print(hmin, hmax, smin, smax, vmin, vmax)

    lower = np.array([hmin,smin,vmin])
    upper = np.array([hmax,smax,vmax])

    mask = cv2.inRange(sharpened, lower, upper)
    
    final_result = cv2.bitwise_and(sharpened,sharpened,mask = mask)

    cv2.imshow('Final Output', final_result)
    cv2.imshow('Mask', mask)
    cv2.imshow("Input", sharpened)
    cv2.waitKey(1)


# cv2.destroyAllWindows()


# image = cv2.imread("1_newScaleSharp.jpg")
# cv2.imshow("Output", image)
# cv2.waitKey(0)


# cv2.destroyAllWindows()
