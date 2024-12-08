import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros((img.shape[:2]), dtype='uint8')

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', circle)

rectangle = cv.rectangle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2+500, img.shape[0]//2+700), 255, -1)
cv.imshow('Rectangle', rectangle)

# rectangle2 = cv.rectangle(blank.copy(), (0,0), (100, 100), 255, -1)
# cv.imshow('Rectangle2', rectangle2)

weird_shape = cv.bitwise_or(circle, rectangle)
cv.imshow('Weird shape', weird_shape)

# weird_shape2 = cv.bitwise_or(weird_shape, rectangle2)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Weird shaped mask image', masked)

cv.waitKey(0)