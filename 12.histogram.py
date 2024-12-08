import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/cats.jpg')
blank = np.zeros((img.shape[:2]), dtype='uint8')

1.
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', circle)

# Load image in grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

mask = cv.bitwise_and(gray, circle)
cv.imshow('Masked', mask)

# Compute Grayscale histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 255])
plt.show()


'''
Explanation of the Grayscale Histogram Graph
X-Axis (Bins):

The x-axis represents pixel intensity values.
Since this is an 8-bit grayscale image, pixel intensities range from 0 to 255:
0: Black
255: White
Values in between are shades of gray.
The bins divide this range into small intervals (typically one bin per intensity value for 8-bit images).

Y-Axis (# of Pixels):
The y-axis represents the number of pixels for each intensity value (or bin).
For example:
If the graph shows a peak at intensity 50, it means a large number of pixels in the image have an intensity of 50.
If the graph is low at intensity 200, it means only a few pixels in the image are that bright.

Why is the X-Axis from 0 to 255?
The x-axis corresponds to grayscale intensity values, which range from 0 to 255 for an 8-bit image.
Each intensity value gets its own bin (256 bins in total, one for each value).

Why is the Y-Axis from 500 to 4000?
The y-axis depends on the image's pixel count and intensity distribution.
It shows how many pixels fall into each intensity bin.
In this graph:
500 (minimum): Few pixels have intensities near these bins.
4000 (maximum): Around intensity 50, about 4000 pixels have this intensity.
The exact range of the y-axis changes depending on the image content.

Key Observations in Your Graph:
The graph peaks around intensity 50, indicating a large number of darker gray pixels.
The graph gradually declines as intensity increases, meaning the image has fewer bright pixels (values closer to 255).
The graph suggests the image is dominated by darker tones (common in dimly lit images).
Histogram Parameters in OpenCV That Control the Axes:
When you calculate a histogram, parameters like histSize and ranges influence the x-axis and y-axis:

histSize=[256]:
Divides the intensity range into 256 bins (one bin per intensity value for 8-bit images).
This is why the x-axis spans 0 to 255.

ranges=[0, 256]:
Defines the range of intensity values considered.
This ensures the x-axis covers all intensity values.
The y-axis scales dynamically based on the number of pixels in each bin, which depends on the image content.
'''
# Note:- You can compute the histograms for the entire image and the masked image: -----> refer the video


# #2.
# # Color Histogram

# mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# masked = cv.bitwise_and(img, img, mask=mask)

# color = ('b', 'g', 'r')

# plt.figure()
# plt.title('Color Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')

# for i, col in enumerate(color):
#     # color_hist = cv.calcHist([img], [i], None, [256], [0, 256])
#     color_hist = cv.calcHist([img], [i], mask, [256], [0, 256])
#     plt.plot(color_hist)
#     plt.xlim([0, 256])

# plt.show()


cv.waitKey(0)