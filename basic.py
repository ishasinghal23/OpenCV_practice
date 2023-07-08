import cv2 as cv

img = cv.imread('images/scene.jpeg')
cv.imshow("Scene", img)

# Converting images to grey scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#Bluring the image
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

#Edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges", canny) 

#Dilate the images
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("Dilated", dilated)

#Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow("Eroded", eroded)

#Resize
resized = cv.resize(img, (500,500),interpolation=cv.INTER_AREA)
cv.imshow("Resized", resized)

#Cropping
cropped = img[0:50, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)