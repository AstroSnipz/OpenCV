import cv2 as cv 

img = cv.imread('Photos/park.jpg')
cv.imshow('Cat', img)

# Averaging
blur = cv.blur(img, (3, 3))
cv.imshow('Blur', blur)

# Gaussian Blur
gaussian_blur = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Blur', gaussian_blur)

# Median blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)