import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Canny edge detection
canny_edge = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny_edge)

# Laplacian: detects edges by calculating the second derivative of an image.
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap)) # absolute is done coz: second-order derivatives can have negative values.,  The np.uint8() function converts the absolute values to an 8-bit integer format (ranging from 0 to 255), which is required for displaying the image using OpenCV.
cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) # It highlights vertical edges in the image.
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1) # It highlights horizontal edges in the image.
cv.imshow('SobelX', sobelx)
cv.imshow('SobelY', sobely)

combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined Sobel', combined_sobel)

cv.waitKey(0)