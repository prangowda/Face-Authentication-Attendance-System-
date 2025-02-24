# **Face Authentication Attendance System in Python**  

This project is a **Face Authentication Attendance System** that uses **Computer Vision and AI** to recognize faces and mark attendance automatically. It captures real-time face data, compares it with stored images, and logs attendance in an Excel sheet.  

---

## **📌 Features**  

✔ **Real-time face recognition** using OpenCV  
✔ **Stores attendance** in an Excel file  
✔ **Automatic authentication** for attendance marking  
✔ **Fast and accurate** face detection  
✔ **Cross-platform support** (Windows, macOS, Linux)  

---

## **🛠️ Technologies Used**  

| **Technology**  | **Purpose**  |  
|-----------------|-------------|  
| **Python**  | Main programming language |  
| **OpenCV**  | Face detection and recognition |  
| **Face Recognition Library**  | Identify and compare faces |  
| **Numpy & Pandas**  | Data handling |  
| **OpenPyXL**  | Excel file management |  

---

## **📂 Project Structure**  

```
/Face_Authentication_Attendance
│── face_attendance.py         # Main script for face recognition
│── train_faces.py             # Script to train face data
│── dataset/                   # Stores face images of registered users
│── attendance.xlsx            # Excel file to store attendance records
│── README.md                  # Documentation
│── requirements.txt           # Dependencies
```

---

## **🔧 Installation Guide**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/prangowda/Face_Authentication_Attendance.git
cd Face_Authentication_Attendance
```

### **2️⃣ Install Dependencies**  
```sh
pip install opencv-python face-recognition numpy pandas openpyxl
```

### **3️⃣ Run the Face Registration Script**  
```sh
python train_faces.py
```
✅ This will capture images of registered users and store them in the dataset.  

### **4️⃣ Run the Face Attendance System**  
```sh
python face_attendance.py
```
✅ It will detect faces and automatically mark attendance in **attendance.xlsx**  

---

## **📜 How It Works**  

1. The system **registers a user’s face**  
2. When a person appears before the camera, the system **compares their face with stored images**  
3. If the face **matches**, attendance is **marked in an Excel file**  
4. If the person is **not found**, they are not recorded  

---

## **📊 Sample Output**  

### **🖼️ Face Registration**  
✅ The system captures 10 images and stores them in `dataset/`  

### **📋 Attendance Sheet (attendance.xlsx)**  
| Name | Time |
|------|---------------------|
| Alice | 2025-02-12 10:30:45 |
| Bob | 2025-02-12 10:35:12 |

---

## **🚀 Future Enhancements**  
✅ Deploy on **CCTV cameras** for real-time monitoring  
✅ Build a **web-based** attendance dashboard  
✅ Store attendance **in a database (MySQL, Firebase)**  

---

## **🤝 Contributing**  
We welcome contributions! Follow these steps:  
1. **Fork** the repository  
2. **Create** a new branch (`feature-xyz`)  
3. **Commit** your changes  
4. **Push** to your branch and submit a **Pull Request**  
