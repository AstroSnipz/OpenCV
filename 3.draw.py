import cv2 as cv 
import numpy as np

# creating a blank image
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# coloring a part of the image with certain color
blank[200:300, 300:400] = (4,55,26)
cv.imshow('colored part', blank)

# draw a rectangle
rectangle = cv.rectangle(blank, (0,0), (250,500), (0,0,255), thickness=2)
cv.imshow('Rectangle', rectangle)

# Draw a circle
circle = cv.circle(blank, (blank.shape[1]//2, blank.shape[1]//2),  50, (0,0,255), thickness=-1)
cv.imshow('Circle', circle)

# Draw a line
line = cv.line(blank, (0,0), (250, 250), (0,255,0), thickness=4)
cv.imshow('Line', line)

# writing a text
cv.putText(blank, 'OpenCV', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), 2)
cv.imshow('Text', blank)

cv.waitKey(0)