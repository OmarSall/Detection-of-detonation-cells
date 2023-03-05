#python tryingSthNew.py -i 1.jpg

# import the necessary packages
import argparse
import imutils
import cv2
import numpy as np

ddepth = cv2.CV_16S
kernel_size = 3


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

#defining a kernel
k_sharped = np.array([[0,-1,0],
                     [-1,5,-1],
                     [0,-1,0]])

#defining a kernel
Gaussian_blur = np.array([[1,2,1],
                          [2,4,2],
                          [1,2,1]])


# sharpened = cv2.filter2D(image, -1, k_sharped)

blurred = cv2.filter2D(image, -1, Gaussian_blur)

resized = imutils.resize(blurred, width=1200, height = 500)

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# Apply Laplace function
dst = cv2.Laplacian(gray, ddepth, ksize=kernel_size)
# converting back to uint8
abs_dst = cv2.convertScaleAbs(dst)

sharpened1 = cv2.filter2D(gray, -1, k_sharped)

edged = cv2.Canny(gray, 30, 150)

lines = cv2.HoughLinesP(edged,rho=1,theta = np.pi/180,threshold = 20, minLineLength=90, maxLineGap=10)

# N = lines.shape[0]
# for i in range(N):
#     for x1,y1,x2,y2 in lines[i]:
#         cv2.line(resized,(x1,y1),(x2,y2),(0,0,255),2)


# erode = cv2.erode(edged, None, iterations=1)

thresh = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY_INV)[1]


kernel = np.ones((3, 3), np.uint8)

erode = cv2.erode(thresh, kernel, iterations=4)

cv2.imshow("Contours",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()