# Face Recognition Attendance System

A comprehensive desktop application built in Python for automating student attendance using facial recognition.

## Features
- **Student Record Management**: Add, update, delete, and view student details connected to an SQL database.
- **Automated Dataset Generation**: Automatically captures and crops face images for the AI dataset using Haar Cascades.
- **AI Model Training**: Uses Local Binary Patterns Histograms (LBPH) to train the facial recognition classifier.
- **Real-Time Detection**: Opens the webcam, detects faces, and accurately recognizes registered students.
- **Automated Attendance Logging**: Automatically logs recognized students as "Present" with a timestamp into a CSV file.
- **Attendance Interface**: Import, view, and export attendance records straight from the dashboard.

## Tech Stack
- **Python 3**
- **Tkinter** (Graphical User Interface)
- **OpenCV (`opencv-contrib-python`)** (Image processing and Face Recognition)
- **PyODBC** (SQL Server Database Connection)
- **Pillow (PIL)** (Image handling in Tkinter)

## Setup
1. Clone the repository.
2. Install the required packages: `pip install opencv-contrib-python pyodbc pillow numpy`
3. Ensure you have Microsoft SQL Server installed with a database named `face_recognition` and a table named `student`.
4. Run `face app hamza.py` to launch the dashboard.
