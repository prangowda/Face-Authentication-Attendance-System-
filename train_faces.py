import cv2
import os

# Create dataset folder if not exists
dataset_path = "dataset"
if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

# Initialize camera
camera = cv2.VideoCapture(0)
name = input("Enter your name: ")

count = 0
while count < 10:
    ret, frame = camera.read()
    if not ret:
        break
    
    file_path = f"{dataset_path}/{name}_{count}.jpg"
    cv2.imwrite(file_path, frame)
    
    cv2.imshow("Capturing Face", frame)
    cv2.waitKey(500)
    count += 1

camera.release()
cv2.destroyAllWindows()
print("Face data collected successfully!")
