import cv2
import numpy as np

def resize_img(path, scale_percent):

    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    print('Original Dimensions : ',img.shape)

    # scale_percent = 15 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    print('Resized Dimensions : ', resized.shape)
    
    return resized



new_image = resize_img("image.jpg", 15)

#defining a kernel
k_sharped = np.array([[-1,-1,-1],
                     [-1,9,-1],
                     [-1,-1,-1]])

sharpened = cv2.filter2D(new_image, -1, k_sharped)

ret, thresh = cv2.threshold(sharpened, 127,255,cv2.THRESH_BINARY)
cannyImage = cv2.Canny(sharpened, 50,100)

cv2.imshow("Original", sharpened)
cv2.imshow("thresholded", thresh)
cv2.imshow("Canny", cannyImage)

cv2.waitKey(0)
cv2.destroyAllWindows()