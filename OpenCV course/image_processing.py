import cv2

img = cv2.imread("image.jpg", -1)
resized = cv2.resize(img, (800, 800))
# px = img[100,100]
# print(px)

#ROI - REGION OF IMAGE

roi = cv2.selectROI(resized)

#cropping selected ROI

roi_cropped = resized[int(roi[1]): int(roi[1] + roi[3]), int(roi[0]): int(roi[0] + roi[2])]

cv2.imshow("ROI image", roi_cropped)
cv2.imwrite("cropped.jpg", roi_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()