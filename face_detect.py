import cv2 as cv 

# Detecting faces in an Image
img = cv.imread('Photos/lady.jpg')
cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=3)
print(faces_rect)
print(len(faces_rect))

for x, y, w, h in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), 2)

cv.imshow('Detected Face', img)

# Detecting faces in a video
# capture = cv.VideoCapture("Videos/kitten.mp4")

# while True:
#     isTrue, frame = capture.read() 
#     if not isTrue:
#         break 

#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#     faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8)

#     for (x, y, w, h) in faces_rect:
#         cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

#     print(len(faces_rect))
#     cv.imshow('Video with Face Detection', frame)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# # Release the video capture object and close windows
# capture.release()
# cv.destroyAllWindows()

cv.waitKey(0)