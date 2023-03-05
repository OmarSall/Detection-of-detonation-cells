import cv2

def resize_img(path, scale_percent):

    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)

    print('Original Dimensions : ',img.shape)

    # scale_percent = 15 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    print('Resized Dimensions : ', resized.shape)
    
    return resized


# image = resize_img("image.jpg", 20)

# cv2.imwrite("1_newScale.jpg", image)

# cv2.imshow("after merging", image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()