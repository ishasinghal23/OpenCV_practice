import cv2 as cv
import numpy as np

img = cv.imread('images\scene.jpeg')
cv.imshow("Scene", img)

#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

'''
-x --> left
-y --> up
x --> right
y --> down
'''

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width)= img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow("Rotated", rotated)

# In this black triangle are also rotated as the part of the image
rotated_again = rotate(rotated, 45)
cv.imshow("Rotated", rotated_again)

# Flipping
# 0->vertical 1->horizontal -1->both horizontally and vertucally together
flip = cv.flip(img, 0)
cv.imshow('Flip', flip)

cv.waitKey(0)