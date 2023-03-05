import argparse
import cv2 as cv
# construct the argument parse and parse the arguments

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                    help = "name of the image")

args = vars(ap.parse_args())

#display a message to the user
# print("Hi there {}, it's nice to meet You!".format(args["name"]))

im = cv.imread(args["image"])
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cnt = contours[4]

new = cv.drawContours(im, [cnt], 0, (0,255,0), 3)

cv.imshow("Outline", im)
cv.imshow("Outlinse", new)
cv.waitKey(0)
cv.destroyAllWindows()