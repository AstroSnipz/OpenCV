import cv2 as cv 
import matplotlib.pyplot as plt 

img = cv.imread('Photos/nature.png')
cv.imshow('Cat', img)

dimensions = (img.shape[1]//2, img.shape[0]//2)
resized = cv.resize(img, dimensions, interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Gray scale
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
print('Gray', gray)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(resized, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB
lab = cv.cvtColor(resized, cv.COLOR_BGR2Lab)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(resized, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# plt.imshow(resized)
# plt.show()

# HSV to BGR
hsv_to_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv_to_bgr', hsv_to_bgr)

# LAB to BGR
lab_to_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('lab_to_bgr', hsv_to_bgr)

cv.waitKey(0)
