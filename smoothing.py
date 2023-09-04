import cv2 as cv

img = cv.imread('images\dogs.jpg')
cv.imshow("Dogs", img)

#Averaging
average = cv.blur(img,(3,3))
cv.imshow("Average blur", average)

#Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gaussian blur", gauss)

#Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median blur", median)

#Lateral Bluring (most effective)
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("Bi-Lateral blur", bilateral)

cv.waitKey(0)