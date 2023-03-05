import cv2
# 0 - gray scale
# 1 - RGB
# -1 leave image as it was before
img = cv2.imread("image.jpg", -1)
print(img.shape)
resized = cv2.resize(img, (800, 800))

cv2.imshow('OS_image', resized)
cv2.waitKey()
cv2.destroyAllWindows()