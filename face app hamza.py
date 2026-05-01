
from student_record import Face_Recognition_System1
from train import Train
from attendance import Attendance
from face_recognition import Face_Recognition

import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x690+0+0")
        self.root.title("Face Recognition System")
        self.root.resizable(width=0, height=0)

        # 1st image
        img1 = Image.open(r"D:\chrome downloads\banner2.jfif")
        img1 = img1.resize((400, 250), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoimg1).place(x=0, y=0, width=400, height=250)

        # 2nd image
        img2 = Image.open(r"D:\chrome downloads\1person.jfif")
        img2 = img2.resize((400, 250), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.photoimg2).place(x=400, y=0, width=400, height=250)

        # 3rd image
        img3 = Image.open(r"D:\chrome downloads\3face.jfif")
        img3 = img3.resize((400, 250), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        Label(self.root, image=self.photoimg3).place(x=800, y=0, width=400, height=250)

        # background image
        img4 = Image.open(r"D:\chrome downloads\bg.png")
        img4 = img4.resize((1200, 690), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        label4 = Label(self.root, image=self.photoimg4)
        label4.place(x=0, y=250, width=1200, height=690)

        # Title
        Label(
            label4,
            text="HAMZA FACE ATTENDANCE SYSTEM",
            font=("times new roman", 20, "bold"),
            bg="white",
            fg="red"
        ).place(x=0, y=0, width=1200, height=30)

        # ---------------- BUTTON 1 (STUDENT RECORD) ----------------
        img5 = Image.open(r"D:\chrome downloads\studentdetails.jfif")
        img5 = img5.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(label4, image=self.photoimg5, command=self.student_link, cursor="hand2")
        b1.place(x=50, y=50, width=195, height=195)

        Button(label4, text="Student Record",
               command=self.student_link,
               font=("times new roman", 13, "bold"),
               bg="darkblue", fg="white", cursor="hand2").place(x=65, y=255, width=180, height=30)

        # ---------------- BUTTON 2 (FACE DETECTOR) ----------------
        img6 = Image.open(r"D:\chrome downloads\iron4.png")
        img6 = img6.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        Button(label4, image=self.photoimg6, cursor="hand2", command=self.face_data_link).place(x=270, y=50, width=200, height=200)

        Button(label4, text="Face Detector",
               font=("times new roman", 13, "bold"),
               bg="darkblue", fg="white", cursor="hand2", command=self.face_data_link).place(x=280, y=255, width=180, height=30)

        # ---------------- BUTTON 3 (ATTENDANCE) ----------------
        img7 = Image.open(r"D:\chrome downloads\attend.jfif")
        img7 = img7.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        Button(label4, image=self.photoimg7, cursor="hand2", command=self.attendance_link).place(x=500, y=50, width=200, height=200)

        Button(label4, text="Attendance",
               font=("times new roman", 13, "bold"),
               bg="darkblue", fg="white", cursor="hand2", command=self.attendance_link).place(x=505, y=255, width=180, height=30)

        # ---------------- BUTTON 4 (TRAIN DATA) ----------------
        img8 = Image.open(r"D:\chrome downloads\trainn.jfif")
        img8 = img8.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        Button(label4, image=self.photoimg8, cursor="hand2", command=self.train_link).place(x=720, y=50, width=200, height=200)

        Button(label4, text="Train Data",
               font=("times new roman", 13, "bold"),
               bg="darkblue", fg="white", cursor="hand2", command=self.train_link).place(x=730, y=255, width=180, height=30)

        # ---------------- BUTTON 5 (PHOTOS) ----------------
        img9 = Image.open(r"D:\chrome downloads\photo.jfif")
        img9 = img9.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        # Added command=self.open_img here so the image is clickable
        Button(label4, image=self.photoimg9, command=self.open_img, cursor="hand2").place(x=950, y=50, width=200, height=200)

        Button(label4, text="Photos", command=self.open_img,
               font=("times new roman", 13, "bold"),
               bg="darkblue", fg="white", cursor="hand2").place(x=955, y=255, width=180, height=30)

        # ---------------- BUTTON 6 (DEVELOPER) ----------------
        img10 = Image.open(r"D:\chrome downloads\develop.jfif")
        img10 = img10.resize((200, 100), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        Button(label4, image=self.photoimg10, cursor="hand2").place(x=45, y=300, width=200, height=100)

        Button(label4, text="Developer",
               font=("times new roman", 13, "bold"),
               bg="darkblue", fg="white", cursor="hand2").place(x=50, y=405, width=180, height=30)

        # ---------------- BUTTON 7 (EXIT) ----------------
        img11 = Image.open(r"D:\chrome downloads\exitt.jfif")
        img11 = img11.resize((200, 100), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        Button(label4, image=self.photoimg11, cursor="hand2", command=self.root.quit).place(x=270, y=300, width=200, height=100)

        Button(label4, text="EXIT",
               font=("times new roman", 13, "bold"),
               bg="darkblue", fg="white", cursor="hand2",
               command=self.root.quit).place(x=275, y=405, width=180, height=30)

    # Functions
    def student_link(self):
        # Ensure you have Face_Recognition_System1 defined in your other file
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition_System1(self.new_window)

    def train_link(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def attendance_link(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def face_data_link(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def open_img(self):
        # Opens your folder on the D: drive
        os.startfile(r"D:\chrome downloads\face recognition\data")

if __name__ == "__main__":
    root = Tk()
    obj = face_recognition_system(root)
    root.mainloop()
