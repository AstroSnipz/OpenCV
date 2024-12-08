import cv2 as cv 

'''rescaling videos'''
# def rescaleFrame(frame, scale=0.75):

#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)

#     dimensions = (width, height)
#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) 

# '''Interpolation calculates the values of new pixels in the resized image based on the values
#  of existing pixels in the original image. This is especially important when enlarging or
#    shrinking images, as new pixels need to be generated.
   
#    cv.INTER_AREA: Best suited for shrinking (reducing the size of) an image.'''


# capture = cv.VideoCapture('Videos/dog.mp4')
# while True:

#     isTrue, frame = capture.read()
#     resized_frame = rescaleFrame(frame)
#     cv.imshow('Cat', frame)
#     cv.imshow('Resized_cat', resized_frame)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()


'''--------------------------------------------------------------------------------------------------------------'''
'''rescaling images'''

img = cv.imread("Photos/wanda.jpeg")

print(img.shape)


width = int(img.shape[1] * 0.2)
height = int(img.shape[0] * 0.2)

dimensions = (width, height)
print(dimensions)
resized_img = cv.resize(img, dimensions, interpolation=cv.INTER_AREA)
cv.imshow('Bird', resized_img)

cv.waitKey(0)