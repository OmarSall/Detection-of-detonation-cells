#python derivatives.py -i 1.jpg

# import the necessary packages
import argparse
import imutils
import cv2
import numpy as np
import matplotlib.pyplot as plt
#importing scikit-image submodule to compute histograms
from skimage import exposure as iml 

def nothing(x):
    pass


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

blur = cv2.GaussianBlur(grad,(5,5),0)

grad_x2 = cv2.Sobel(abs_grad_x, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
grad_y2 = cv2.Sobel(abs_grad_y, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
abs_grad_x2 = cv2.convertScaleAbs(grad_x2)
abs_grad_y2 = cv2.convertScaleAbs(grad_y2)

grad2 = cv2.addWeighted(abs_grad_x2, 0.5, abs_grad_y2, 0.5, 0)

# ret, thresh = cv2.threshold(grad, 127,255,cv2.THRESH_BINARY)


#defining a kernel
k_sharped = np.array([[0,-1,0],
                     [-1,5,-1],
                     [0,-1,0]])

sharpened = cv2.filter2D(abs_grad_x2, -1, k_sharped)

edged = cv2.Canny(sharpened, 205, 255)
# cv2.imshow("Grad2",grad2)

cv2.imshow("Gradxx",abs_grad_x2)
cv2.imshow("Sharpened_gradXx",sharpened)
cv2.imshow("Canny_FROMSHARP",edged)
cv2.imshow("Original",resized)

cv2.waitKey(0)
cv2.destroyAllWindows()

# hist, bins= iml.histogram(abs_grad_x2)

# plt.xlabel('normalized gray level')
# plt.ylabel('pixels')
# plt.plot(bins,hist)
# plt.show()