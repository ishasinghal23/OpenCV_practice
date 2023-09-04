import cv2 as cv
'''
# Reading images in its orginal size
img = cv.imread('images\cats.jpeg')
cv.imshow('Cat', img)

cv.waitKey(0)
'''

#Reading videos

# If we put 0 as an argument we can access web cam 
capture = cv.VideoCapture('videos\cdc.mp4')

#We read video frame by frame
while True:
    #This returns the frame and a boolean sayingif the frame was read successfully or not
    isTrue, frame = capture.read()
    #This command is to show each frame
    cv.imshow('Video', frame)
    
    # This is to stop video from playing indefinetly
    if cv.waitKey(20) & 0xFF==ord('d'): # if letter d is pressed then close the video
        break
    
capture.release()
capture.destroyAllWindows()
cv.waitKey(0)