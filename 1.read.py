import cv2 as cv 

'''reading images'''

# img = cv.imread('photos/birds.jpg')
# cv.imshow('cat', img)
#cv.waitKey(0)

'''reading videos'''

capture = cv.VideoCapture("Videos/kitten.mp4") # here capture becomes an object of opencv class

while True:
    isTrue, frame = capture.read()  # isTrue indicates if the frame was successfully read, and frame contains the image data of the current frame

    # if(not isTrue):
    #    break
    cv.imshow('Video', frame) # displays individual frame
    
    if cv.waitKey(20) & 0xFF == ord('d'):  # Waits for 20ms for a key press; if 'd' is pressed, the loop breaks
        break
capture.release() # Resources like memory and file handles are freed.
cv.destroyAllWindows()
