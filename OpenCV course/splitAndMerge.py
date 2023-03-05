import cv2

img = cv2.imread("image.jpg", -1)
resized = cv2.resize(img, (800, 800))

g,b,r = cv2.split(resized)

cv2.imshow("Green image", g)
cv2.imshow("Red image", r)
cv2.imshow("Blue image", b)


img1 = cv2.merge((g,b,r))
cv2.imshow("after merging", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()