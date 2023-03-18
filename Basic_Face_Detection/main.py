import face_recognition
import cv2
import numpy as np
import csv 
import os
import glob 
from datetime import datetime 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 0 for webcam
video_capture = cv2.VideoCapture(0)
# address = 'https://192.168.1.3:8080/video'
# video_capture.open(address)

# load all images using glob
images = glob.glob("photos/*.*")
known_face_encodings = []
known_face_name = []

# loop through all images and encode them
for image in images:

    face = face_recognition.load_image_file(image)
    face_encoding = face_recognition.face_encodings(face)[0]
    
    known_face_encodings.append(face_encoding)
    known_face_name.append(os.path.splitext(os.path.basename(image))[0])
    
    
students = known_face_name.copy()
print("Initially: ", students)

face_locations = []
face_encodings = []
face_names = []
status = True

date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# create file if not exists
if not os.path.exists('attendance.csv'):
    open(date + '.csv', 'a+').close()
    
# open the file
fp = open(date + '.csv', 'a+', newline='')
file_write = csv.writer(fp)

# read video frame by frame
while True:
    _ , frame = video_capture.read()
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    

    if status: 
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding) # face_encodings is from webcam
            name = ''
            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)
            
            if matches[best_match_index]:
                name = known_face_name[best_match_index]
                
                if name in known_face_name:
                    if name in students:
                        students.remove(name) # remove the name from the list for avoiding duplication
                        print(students)
                        date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                        file_write.writerow([name, date])
                        
    cv2.imshow('Video', frame)
    key = cv2.waitKey(1)
    
    if key == ord('q'):
        break
    
video_capture.release()
cv2.destroyAllWindows()
fp.close()