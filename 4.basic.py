import cv2 as cv 

# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)

# #m1. converting an image to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # 2. Blur
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur) 
# '''
# Note: 
# cv.BORDER_DEFAULT:- When applying convolution (like a blur) to an image, each pixel in the image is processed by looking at its surrounding pixels within a kernel (like a 3x3 or 7x7 matrix). 
# However, for pixels on the edges or corners of the image, some of the neighboring pixels would be outside the image boundary (i.e., there are no pixels beyond the edges of the image).
# Handling the Image Border. The cv.BORDER_DEFAULT (and other border handling types) is used to define how OpenCV should handle these edge cases when it tries to access pixels outside the 
# image boundary.
# '''

# # 3. Edge Cascade
# canny = cv.Canny(img, 120, 140)
# cv.imshow('Canny Edges', canny)
# # u can reduce the edges by blurring the image
# canny_blur = cv.Canny(blur, 120, 140)
# cv.imshow('blured canny edges',canny_blur)



# # 4. Dilating the image
# dilate = cv.dilate(canny_blur, (7,7), iterations=1)
# cv.imshow('Dilated', dilate)
# # Eroded
# erode = cv.erode(dilate, (7,7), iterations=1)
# cv.imshow('Erode', erode)




# 5. Resizing
img_large = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat_large', img_large)

resized = cv.resize(img_large, (250, 250), interpolation=cv.INTER_AREA)
cv.imshow('Resized_cat', resized)

# Cropping
cropped_image = resized[:200]
cv.imshow('Cropped_image', cropped_image)

cv.waitKey(0)