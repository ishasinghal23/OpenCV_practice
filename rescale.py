import cv2 as cv

img = cv.imread('images\cats.jpeg')
cv.imshow("Cat", img)

def rescale(frame, scale=0.75):
    width = int(frame.shape[1] * scale) 
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# The above one works for beoth but we have a method capture.set for video resizing 
def changeRes(height, width):
    #This is more appropriate for live video and rescale function we created is good for already existing videos and images in the local computer.
    capture.set(3,width) # 3 references width
    capture.set(4,height) # 4 refernces height
    


# If we put 0 as an argument we can access web cam 
capture = cv.VideoCapture('videos\cdc.mp4')

#We read video frame by frame
while True:
    #This returns the frame and a boolean sayingif the frame was read successfully or not
    isTrue, frame = capture.read()
    
    frame_resized = rescale(frame) # Similar can be used for images as well
    
    #This command is to show each frame
    cv.imshow('Video', frame)
    cv.imshow("Video Resized", frame_resized)
    
    # This is to stop video from playing indefinetly
    if cv.waitKey(20) & 0xFF==ord('d'): # if letter d is pressed then close the video
        break
    
capture.release()
capture.destroyAllWindows()

cv.waitKey(0)