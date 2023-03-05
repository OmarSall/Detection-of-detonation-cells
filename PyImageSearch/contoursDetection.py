#python contoursDetection.py -i tetris.jpg

# import the necessary packages
import argparse
import imutils
import cv2
import numpy as np
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


edged = cv2.Canny(gray, 30, 150)

# erode = cv2.erode(edged, None, iterations=1)

thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]


kernel = np.ones((3, 3), np.uint8)

erode = cv2.erode(thresh, kernel, iterations=4)

# find contours (i.e., outlines) of the foreground objects in the
# thresholded image
cnts = cv2.findContours(erode.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()
# cv2.imshow("Contours", erode)
# cv2.imshow("Contours1", thresh)
	
	
# loop over the contours
for c in cnts:
	# draw each contour on the output image with a 3px thick purple
	# outline, then display the output contours one at a time
	cv2.drawContours(output, [c], -1, (240, 0, 159), 8)
	
	
# draw the total number of contours found in purple
text = "I found {} objects!".format(len(cnts))
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	(240, 0, 159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)