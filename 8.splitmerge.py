import cv2 as cv 
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Img', img)

# split an image
b, g, r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merging the images
merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)

# reconstructing the image n showing the actual colors after splitting (optional)
blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

# note:- when merging color channels in OpenCV using cv.merge(), each channel should be a 2D array representing a single channel of pixel intensities.

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)


cv.waitKey(0)
