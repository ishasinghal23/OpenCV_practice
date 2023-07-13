import cv2 as cv
import numpy as np

'''
There are two ways to draw on an image:
1. drwaing on this static image
2. creating a black image and draw on that
'''


blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Black', blank)
'''
# 1. Paint the image a certain color
# blank[200:300, 300:400] = 0,0,255
# cv.imshow("Green", blank)

# 2. Draw a rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2)
#To fill this rectangle we can take thickness=cv.FILLED or -1 instead of 2.
cv.imshow("Rectangle", blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow("Circle", blank)

#Draw a line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=2)
#Changing the coordinates
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow("Line", blank)
'''

#Write text
cv.putText(blank, "Hello", (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)