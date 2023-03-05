import cv2

img = cv2.imread("image.jpg", -1)
resized = cv2.resize(img, (800, 800))

color_change = cv2.cvtColor(resized, cv2.COLOR_RGB2LAB)

cv2.imshow("Changed color", color_change)
cv2.waitKey(0)
cv2.destroyAllWindows()
