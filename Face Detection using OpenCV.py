# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 23:14:30 2019

@author: alokc
"""
### The below code is used to detect faces using OpenCV.  ###
 
import cv2

# Loading the cascades
face_cascade = cv2.CascadeClassifier('./haarcascade/haarcascade_frontalface_default.xml')


# Defining a function that will do the detections
def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
    return frame

# Doing some Face Recognition with the webcam
video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        canvas = detect(gray, frame)
        cv2.imshow('Video', canvas)

#Press 'q' to exit        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()