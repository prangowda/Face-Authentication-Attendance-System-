import cv2
import face_recognition
import numpy as np
import os
import pandas as pd
from datetime import datetime

dataset_path = "dataset"
attendance_file = "attendance.xlsx"

# Load face encodings
known_face_encodings = []
known_face_names = []

for file in os.listdir(dataset_path):
    image = face_recognition.load_image_file(f"{dataset_path}/{file}")
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)
    known_face_names.append(file.split("_")[0])

# Start webcam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

            # Mark attendance
            df = pd.read_excel(attendance_file)
            if name not in df["Name"].values:
                new_data = {"Name": name, "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                df = df.append(new_data, ignore_index=True)
                df.to_excel(attendance_file, index=False)

        # Display result
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    cv2.imshow("Face Authentication Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
