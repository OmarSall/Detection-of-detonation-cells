# # import required libraries
import cv2
import numpy as np
from resizeFunc import *
# def nothing(x):
#    pass
   
# # Create a black image, a window
# img = np.zeros((300,650,3), np.uint8)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# window_name = 'HSV Color Palette'
# cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

# # create trackbars for color change
# cv2.createTrackbar('H',window_name,0,179,nothing)
# cv2.createTrackbar('S',window_name,0,255,nothing)
# cv2.createTrackbar('V',window_name,0,255,nothing)
# while(True):
#    cv2.imshow(window_name,img)
#    key = cv2.waitKey(1) & 0xFF
#    if key == ord('q'):
#       break
      
#    # get current positions of four trackbars
#    h = cv2.getTrackbarPos('H',window_name)
#    s = cv2.getTrackbarPos('S',window_name)
#    v = cv2.getTrackbarPos('V',window_name)
#    img[:] = [h,s,v]
#    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
# cv2.destroyAllWindows()



def mouseRGB(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        colorsB = image[y,x,0]
        colorsG = image[y,x,1]
        colorsR = image[y,x,2]
        colors = image[y,x]

        hsv_value = np.uint8([[[colorsB, colorsG, colorsR]]])
        hsv = cv2.cvtColor(hsv_value, cv2.COLOR_BGR2HSV)

        print("HSV : ", hsv)
        # print("Red: ",colorsR)
        # print("Green: ",colorsG)
        # print("Blue: ",colorsB)
        # print("BRG Format: ",colors)
        print("Coordinates of pixel: X: ",x,"Y: ",y)

# Read an image, a window and bind the function to window
image = resize_img("image.jpg", 20)

#defining a kernel
k_sharped = np.array([[0,-1,0],
                     [-1,5,-1],
                     [0,-1,0]])


sharpened = cv2.filter2D(image, -1, k_sharped)



cv2.namedWindow('mouseRGB')
cv2.setMouseCallback('mouseRGB',mouseRGB)

#Do until esc pressed
while(1):
    cv2.imshow('mouseRGB',sharpened)
    if cv2.waitKey(20) & 0xFF == 27:
        break
#if esc pressed, finish.
cv2.destroyAllWindows()