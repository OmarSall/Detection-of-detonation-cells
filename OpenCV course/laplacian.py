import cv2
import numpy as np
from resizeFunc import *

ddepth = cv2.CV_16S
kernel_size = 3

new_image = resize_img("image.jpg", 15)

#defining a kernel
# k_sharped = np.array([[-1,-1,-1],
                    #  [-1,9,-1],
                    #  [-1,-1,-1]])

# sharpened = cv2.filter2D(new_image, -1, k_sharped)

# Remove noise by blurring with a Gaussian filter
src = cv2.GaussianBlur(new_image, (3, 3), 0)

# Convert the image to grayscale
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# Apply Laplace function
dst = cv2.Laplacian(src_gray, ddepth, ksize=kernel_size)

# converting back to uint8
abs_dst = cv2.convertScaleAbs(dst)


cv2.imshow("Input", new_image)
cv2.imshow("Image", abs_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()