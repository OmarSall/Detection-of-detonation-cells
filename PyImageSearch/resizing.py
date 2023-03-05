import cv2
import imutils

image = cv2.imread("1.jpg", 0)


resized = imutils.resize(image, width=1200, height = 500)
output = resized.copy()
cv2.rectangle(output, (250, 130), (520, 290), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
# cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)