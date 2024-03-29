import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images\cats.jpeg')
cv.imshow("Cats", img)

# plt.imshow(img)
# plt.show()

#BGR to GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to L+a+b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

#hsv to Bgr
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV ---> BGR", hsv_bgr)

#LAB to Bgr
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("LAB ---> BGR", lab_bgr)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)