import cv2

img = cv2.imread("image.jpg", cv2.IMREAD_COLOR)
resized = cv2.resize(img, (800, 800))

img1 = cv2.imread("image1.jpg", cv2.IMREAD_COLOR)
resized1 = cv2.resize(img1, (800, 800))


blended_img = cv2.addWeighted(resized,1, resized1, 0.5, 0.0)


cv2.imshow("blended", blended_img)
cv2.waitKey(0)
cv2.destroyAllWindows()