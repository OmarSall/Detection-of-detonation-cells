# USAGE
# python load_image.py --image 1.jpg

import argparse
import cv2

# construct the argument parse and parse the arguments

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--image", required = True,
                    help = "image name")

args = vars(ap.parse_args())


image = cv2.imread(args["image"])
(h, w, c) = image.shape[:3]

print("width: {} pixels".format(w))
print("height: {} pixels".format(h))
print("channels: {}".format(c))

cv2.imshow("Image", image)
cv2.waitKey(0)

cv2.imwrite("newImage.jpg", image)