import cv2 as cv 
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# 1. translation
# move an image (img) horizontally or vertically by specified amounts.
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x -----> left
# -y -----> Up
# x -----> right
# y -----> down

translated_img = translate(img, -200, 200)
cv.imshow('Translated', translated_img)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# Flip
flip = cv.flip(img, 1)
cv.imshow('Flip', flip)

# Crop
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)