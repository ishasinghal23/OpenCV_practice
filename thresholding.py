import cv2 as cv
#Thresholding of an image is way of converting the image into binary form

img = cv.imread('images\dogs.jpg')
cv.imshow("Dogs", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple Thresholding", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Thresholded Inverse", thresh_inv)

# Adaptive Thresholding (here the thresholded value is choosen by the computer)
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11,3)
cv.imshow("Adaptive Threshold", adaptive_thresh)


cv.waitKey(0)