import os
import cv2 as cv 
import numpy as np 

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'C:\Users\sharon sajan\Downloads\opencv-course-master\opencv-course-master\Resources\Faces\train'

features = []
labels = []

def create_train():
    for person in people:

        person_folder = os.path.join(DIR, person)
        images = os.listdir(person_folder)
        label = people.index(person)

        for each_image in images:

            img_array = cv.imread(f'{person_folder}/{each_image}')
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for x, y, w, h in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]

                features.append(faces_roi)
                labels.append(label)

create_train()

print('..............Training done...............')

features = np.array(features, dtype='object') # When you set dtype='object', this restriction is relaxed, and NumPy no longer attempts to create a homogeneous array(i.e., arrays with same shape).
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
# Train the recognizer on the features list and the labels list
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
