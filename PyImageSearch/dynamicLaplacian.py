#python dynamicLaplacian.py -i 1.jpg

# import the necessary packages
import argparse
import imutils
import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars', 900,120)
cv2.createTrackbar('Lower_thresh', 'Trackbars',0,255,nothing)
cv2.createTrackbar('Upper_thresh', 'Trackbars',255,255,nothing)


while True:



    scale = 1
    delta = 0
    ddepth = cv2.CV_16S

    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
        help="path to input image")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])

    resized = imutils.resize(image, width=1000, height = 400)

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray,(3,3),0)
    # blur1 = cv2.GaussianBlur(blur,(3,3),0)

    #SOBEL
    grad_x = cv2.Sobel(blur, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    grad_y = cv2.Sobel(blur, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)

    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)


    grad_x2 = cv2.Sobel(grad, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    grad_y2 = cv2.Sobel(abs_grad_y, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    abs_grad_x2 = cv2.convertScaleAbs(grad_x2)
    abs_grad_y2 = cv2.convertScaleAbs(grad_y2)

    grad2 = cv2.addWeighted(abs_grad_x2, 0.5, abs_grad_y2, 0.5, 0)

    


    thresh_low = cv2.getTrackbarPos('Lower_thresh', 'Trackbars')
    thresh_up = cv2.getTrackbarPos('Upper_thresh', 'Trackbars')

    print(thresh_low,   thresh_up)

    # lower = np.array([thresh_low])
    # upper = np.array([thresh_up])

    edged = cv2.Canny(abs_grad_x2, thresh_low, thresh_up)

    # cv2.imshow("Gradx",abs_grad_x)
    cv2.imshow("Canny_Gradxyx",edged)
    cv2.imshow("Original",resized)
    # cv2.imshow("Canny2",grad2)
    # cv2.imshow("Canny1",grad)
    cv2.waitKey(1)


# # cv2.destroyAllWindows()

