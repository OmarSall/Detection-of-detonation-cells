from resizeFunc import *
from matplotlib import pyplot as plt


# new_image = resize_img("image.jpg", 15)

new_image = cv2.imread("imageOS.jpg", cv2.IMREAD_UNCHANGED)

gray = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)

#Setting Threshold of the gray scale image

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)


# find contours function

contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

i = 0
for contour in contours:
    if i == 0:
        i = 1
        continue
    appox = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)

    cv2.drawContours(new_image, [contour],0, (255,50,255),5)

#finding a center of different shapes

    M = cv2.moments(contour)
    if M['m10'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])

#putting names of the shapes inside the corresponding shapes
    if len(appox) == 3:
        cv2.putText(new_image, 'Triange', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 2)
    elif len(appox) == 4:
        cv2.putText(new_image, 'Quadrilateral', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (50,5,255), 2)
    elif len(appox) == 5:
        cv2.putText(new_image, 'Pentagon', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100,255,255), 2)
    elif len(appox) == 6:
        cv2.putText(new_image, 'Hexagon', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 2)
    else:
        cv2.putText(new_image, 'circle', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,5,255), 2)



cv2.imshow("Shapes", new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()