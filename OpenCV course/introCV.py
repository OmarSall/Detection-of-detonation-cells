import cv2

image_path = "E:\LAPTOP\STUDIA\II st PW LiK\MAGISTERKA\IMAGE PROCESSING COURSES\OpenCV course\image.jpg"

img = cv2.imread(image_path)

# cv2.imshow('image_OS', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows

# print(img.shape)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #RGB to GRAY
# color = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB) #GRAY TO RGB

#RESIZE OF THE IMAGE
resized = cv2.resize(img, (800, 800))

#Putting text on the image
text = cv2.putText(resized, 'Omaris', (100,400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),4)

#Drawing a line on the image
line = cv2.line(resized, (0,0), (800,800), (0,0,512),5)

#Drawing a circle on the image
circle = cv2.circle(resized, (400,400), 200, (0,255,0), 7)

#Drawing a rectangle on the image
rectangle = cv2.rectangle(resized, (100,0), (400,100), (0,0,255), 10)

#Drawing an ellipse on the image
ellipse = cv2.ellipse(resized, (300,300), (100,200), -30,0,360, (50,50,50),10)

cv2.imshow('image_OS', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()


# diretory = r'E:\LAPTOP\STUDIA\II st PW LiK\MAGISTERKA\IMAGE PROCESSING COURSES\OpenCV course'
# filename = 'savedImage.png'
# cv2.imwrite(filename, img)