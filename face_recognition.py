from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pyodbc
import cv2
import os
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.state('zoomed')

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Main Button
        b1 = Button(self.root, text="Start Face Recognition Scanner", command=self.face_recog, cursor="hand2", font=("times new roman", 18, "bold"), bg="darkgreen", fg="white")
        b1.place(x=550, y=380, width=400, height=60)

    # Attendance Logging
    def mark_attendance(self, i, r, n, d):
        with open("attendance.csv", "a+", newline="\n") as f:
            f.seek(0)
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                if len(entry) > 0:
                    name_list.append(entry[0])
            
            # Check if this ID is already logged for today
            # If we want to log multiple times, we can remove the check.
            # Usually, you only log once per session.
            if str(i) not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"{i},{r},{n},{d},{dtString},{d1},Present\n")


    # Face recognition function
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict/300)))

                try:
                    conn = pyodbc.connect(
                        'DRIVER={SQL Server};'
                        'SERVER=DESKTOP-MJ246J1;'
                        'DATABASE=face_recognition;'
                        'Trusted_Connection=yes;'
                    )
                    cursor = conn.cursor()

                    cursor.execute("SELECT name FROM student WHERE student_id=" + str(id))
                    n = cursor.fetchone()
                    n = n[0] if n else "Unknown"

                    cursor.execute("SELECT roll FROM student WHERE student_id=" + str(id))
                    r = cursor.fetchone()
                    r = r[0] if r else "Unknown"

                    cursor.execute("SELECT dep FROM student WHERE student_id=" + str(id))
                    d = cursor.fetchone()
                    d = d[0] if d else "Unknown"
                    
                    conn.close()
                except Exception as e:
                    n, r, d = "Unknown", "Unknown", "Unknown"
                
                if confidence > 77:
                    cv2.putText(img, f"ID:{id}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dep:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(id, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
            
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        haarcascade_path = r"D:\chrome downloads\face recognition\haarcascade_frontalface_default.xml"
        if not os.path.exists(haarcascade_path):
            messagebox.showerror("Error", f"Haarcascade file not found at: {haarcascade_path}", parent=self.root)
            return

        faceCascade = cv2.CascadeClassifier(haarcascade_path)
        
        if not os.path.exists("classifier.xml"):
            messagebox.showerror("Error", "classifier.xml not found. Please train the data first!", parent=self.root)
            return
            
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        if not video_cap.isOpened():
            messagebox.showerror("Error", "Webcam not found or inaccessible.", parent=self.root)
            return

        while True:
            ret, img = video_cap.read()
            if not ret:
                break
                
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition Scanner - Press Enter (13) to Exit", img)

            if cv2.waitKey(1) == 13:
                break
        
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
