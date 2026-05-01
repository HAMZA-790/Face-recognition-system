
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import pyodbc
import cv2
import os


class Face_Recognition_System1:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.state('zoomed')

        # ================= VARIABLES =================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio = StringVar()

        # ================= TITLE =================
        title_lbl = Label(self.root, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman", 35, "bold"),
                          bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ================= MAIN FRAME =================
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=730)

        # ================= LEFT FRAME =================
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=660, height=700)

        # --- Course Info ---
        course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Current course information", font=("times new roman", 12, "bold"))
        course_frame.place(x=5, y=5, width=645, height=120)

        Label(course_frame, text="Department", font=("arial", 11, "bold"), bg="white").grid(row=0, column=0, padx=10,
                                                                                            pady=10)
        dep_combo = ttk.Combobox(course_frame, textvariable=self.var_dep, font=("arial", 11), state="readonly",
                                 width=17)
        dep_combo["values"] = ("Select Department", "Computer Science", "Information Technology",
                               "Software Engineering", "Data Science", "Cyber Security", "Mechanical", "Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

        Label(course_frame, text="Course", font=("arial", 11, "bold"), bg="white").grid(row=0, column=2, padx=10)
        course_combo = ttk.Combobox(course_frame, textvariable=self.var_course, font=("arial", 11), state="readonly",
                                    width=17)
        course_combo["values"] = ("Select Course", "BSCS", "BSIT", "BSE", "MCS", "MIT", "MSCS", "BBA", "MBA")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2)

        Label(course_frame, text="Year", font=("arial", 11, "bold"), bg="white").grid(row=1, column=0, padx=10)
        year_combo = ttk.Combobox(course_frame, textvariable=self.var_year, font=("arial", 11), state="readonly",
                                  width=17)
        year_combo["values"] = ("Select Year", "2021", "2022", "2023", "2024", "2025", "2026")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10)

        Label(course_frame, text="Semester", font=("arial", 11, "bold"), bg="white").grid(row=1, column=2, padx=10)
        sem_combo = ttk.Combobox(course_frame, textvariable=self.var_semester, font=("arial", 11), state="readonly",
                                 width=17)
        sem_combo["values"] = ("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2)

        # --- Student Info ---
        student_info_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                        text="Class Student information", font=("times new roman", 12, "bold"))
        student_info_frame.place(x=5, y=130, width=645, height=250)

        Label(student_info_frame, text="StudentID", font=("arial", 11, "bold"), bg="white").grid(row=0, column=0,
                                                                                                 padx=5, pady=5,
                                                                                                 sticky=W)
        Entry(student_info_frame, textvariable=self.var_std_id, font=("arial", 11), width=15).grid(row=0, column=1,
                                                                                                   padx=5, pady=5)
        Label(student_info_frame, text="Student Name", font=("arial", 11, "bold"), bg="white").grid(row=0, column=2,
                                                                                                    padx=5, pady=5,
                                                                                                    sticky=W)
        Entry(student_info_frame, textvariable=self.var_std_name, font=("arial", 11), width=15).grid(row=0, column=3,
                                                                                                     padx=5, pady=5)

        Label(student_info_frame, text="Class Division", font=("arial", 11, "bold"), bg="white").grid(row=1, column=0,
                                                                                                      padx=5, pady=5,
                                                                                                      sticky=W)
        div_combo = ttk.Combobox(student_info_frame, textvariable=self.var_div, font=("arial", 11), state="readonly", width=13)
        div_combo["values"] = ("Select Division", "A", "B", "C", "D", "E")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=5, pady=5)
        Label(student_info_frame, text="Roll No", font=("arial", 11, "bold"), bg="white").grid(row=1, column=2, padx=5,
                                                                                               pady=5, sticky=W)
        Entry(student_info_frame, textvariable=self.var_roll, font=("arial", 11), width=15).grid(row=1, column=3,
                                                                                                 padx=5, pady=5)

        Label(student_info_frame, text="Gender", font=("arial", 11, "bold"), bg="white").grid(row=2, column=0, padx=5,
                                                                                              pady=5, sticky=W)
        gender_combo = ttk.Combobox(student_info_frame, textvariable=self.var_gender, font=("arial", 11), state="readonly", width=13)
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=5)
        Label(student_info_frame, text="DOB", font=("arial", 11, "bold"), bg="white").grid(row=2, column=2, padx=5,
                                                                                           pady=5, sticky=W)
        dob_entry = DateEntry(student_info_frame, textvariable=self.var_dob, font=("arial", 11), width=13, date_pattern='dd/mm/yyyy')
        dob_entry.grid(row=2, column=3, padx=5, pady=5)

        Label(student_info_frame, text="Email", font=("arial", 11, "bold"), bg="white").grid(row=3, column=0, padx=5,
                                                                                             pady=5, sticky=W)
        Entry(student_info_frame, textvariable=self.var_email, font=("arial", 11), width=15).grid(row=3, column=1,
                                                                                                  padx=5, pady=5)
        Label(student_info_frame, text="Phone No", font=("arial", 11, "bold"), bg="white").grid(row=3, column=2, padx=5,
                                                                                                pady=5, sticky=W)
        Entry(student_info_frame, textvariable=self.var_phone, font=("arial", 11), width=15).grid(row=3, column=3,
                                                                                                  padx=5, pady=5)

        Label(student_info_frame, text="Address", font=("arial", 11, "bold"), bg="white").grid(row=4, column=0, padx=5,
                                                                                               pady=5, sticky=W)
        Entry(student_info_frame, textvariable=self.var_address, font=("arial", 11), width=15).grid(row=4, column=1,
                                                                                                    padx=5, pady=5)
        Label(student_info_frame, text="Teacher Name", font=("arial", 11, "bold"), bg="white").grid(row=4, column=2,
                                                                                                    padx=5, pady=5,
                                                                                                    sticky=W)
        teacher_combo = ttk.Combobox(student_info_frame, textvariable=self.var_teacher, font=("arial", 11), state="readonly", width=13)
        teacher_combo["values"] = ("Select Teacher", "mam aqsa sarfraz", "mam zanaib khali", "sir umer irshad", "sir ali haider", "sir talha")
        teacher_combo.current(0)
        teacher_combo.grid(row=4, column=3, padx=5, pady=5)

        # Radio Buttons
        radio_frame = Frame(Left_frame, bg="white")
        radio_frame.place(x=5, y=385, width=645, height=30)
        Radiobutton(radio_frame, text="Take Photo Sample", variable=self.var_radio, value="Yes", bg="white",
                    font=("arial", 10, "bold")).pack(side=LEFT, padx=10)
        Radiobutton(radio_frame, text="No Photo Sample", variable=self.var_radio, value="No", bg="white",
                    font=("arial", 10, "bold")).pack(side=LEFT, padx=10)

        # ================= BUTTONS =================
        btn_frame = Frame(Left_frame, bg="white")
        btn_frame.place(x=5, y=420, width=645, height=180)

        btn_config = {"font": ("arial", 11, "bold"), "bg": "blue", "fg": "white", "width": 16, "bd": 1, "relief": FLAT}

        Button(btn_frame, text="Save", command=self.add_data, **btn_config).grid(row=0, column=0, padx=1, pady=5)
        Button(btn_frame, text="Update", command=self.update_data, **btn_config).grid(row=0, column=1, padx=1, pady=5)
        Button(btn_frame, text="Delete", command=self.delete_data, **btn_config).grid(row=0, column=2, padx=1, pady=5)
        Button(btn_frame, text="Reset", command=self.reset_data, **btn_config).grid(row=0, column=3, padx=1, pady=5)

        Button(btn_frame, text="Take Photo Sample", command=self.generate_dataset, font=("arial", 12, "bold"),
               bg="blue", fg="white", width=34).grid(row=1, column=0, columnspan=2, padx=1, pady=5)
        Button(btn_frame, text="Update Photo Sample", command=self.generate_dataset, font=("arial", 12, "bold"),
               bg="blue", fg="white", width=34).grid(row=1, column=2, columnspan=2, padx=1, pady=5)

        # ================= RIGHT FRAME =================
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Student Database", font=("times new roman", 12, "bold"))
        Right_frame.place(x=680, y=10, width=800, height=700)

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=785, height=660)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,
                                          column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender",
                                                  "dob", "email", "phone", "address", "teacher", "photo"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        cols = ["dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone",
                "address", "teacher", "photo"]
        
        # Optimized column widths to reduce scrolling
        col_widths = {
            "dep": 130, "course": 60, "year": 50, "sem": 40, "id": 35, 
            "name": 120, "div": 40, "roll": 60, "gender": 60, "dob": 80, 
            "email": 130, "phone": 90, "address": 130, "teacher": 120, "photo": 50
        }
        
        for c in cols:
            self.student_table.heading(c, text=c.upper())
            self.student_table.column(c, width=col_widths[c])

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ================= DATABASE METHODS =================
    def connect_db(self):
        # Update server name if needed
        return pyodbc.connect(
            "DRIVER={SQL Server};SERVER=DESKTOP-MJ246J1;DATABASE=face_recognition;Trusted_Connection=yes;")

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
        else:
            try:
                conn = self.connect_db()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO student VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                    self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                    self.var_std_id.get(), self.var_std_name.get(), self.var_div.get(), self.var_roll.get(),
                    self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(),
                    self.var_address.get(), self.var_teacher.get(), self.var_radio.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details saved!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("", END, values=list(i))
        conn.close()

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        if data:
            self.var_dep.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_semester.set(data[3])
            self.var_std_id.set(data[4])
            self.var_std_name.set(data[5])
            self.var_div.set(data[6])
            self.var_roll.set(data[7])
            self.var_gender.set(data[8])
            self.var_dob.set(data[9])
            self.var_email.set(data[10])
            self.var_phone.set(data[11])
            self.var_address.set(data[12])
            self.var_teacher.set(data[13])
            self.var_radio.set(data[14])

    def update_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Please select a student record", parent=self.root)
        else:
            update = messagebox.askyesno("Update", "Do you want to update this student?", parent=self.root)
            if update > 0:
                conn = self.connect_db()
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE student SET dep=?, course=?, year=?, semester=?, name=?, division=?, roll=?, gender=?, dob=?, email=?, phone=?, address=?, teacher=?, photo_sample=? WHERE student_id=?",
                    (
                        self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                        self.var_std_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(),
                        self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(),
                        self.var_teacher.get(), self.var_radio.get(), self.var_std_id.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Updated successfully!", parent=self.root)

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Select a student to delete", parent=self.root)
        else:
            delete = messagebox.askyesno("Delete", "Delete this record?", parent=self.root)
            if delete > 0:
                conn = self.connect_db()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM student WHERE student_id=?", self.var_std_id.get())
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Deleted successfully!", parent=self.root)

    def reset_data(self):
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")

    # ================= UPDATED CAMERA LOGIC (EXACT D: DRIVE PATH) =================
    def generate_dataset(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Please enter Student ID first", parent=self.root)
        else:
            try:
                # EXACT PATH FROM YOUR SCREENSHOT (USING RAW STRING r"")
                data_dir = r"D:\chrome downloads\face recognition\data"

                if not os.path.exists(data_dir):
                    os.makedirs(data_dir)

                face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
                cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

                if not cap.isOpened():
                    messagebox.showerror("Error", "Webcam not found. Check permissions or connection.",
                                         parent=self.root)
                    return

                img_id = 0
                while True:
                    ret, frame = cap.read()
                    if not ret: break

                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        img_id += 1
                        face_roi = gray[y:y + h, x:x + w]
                        face_roi = cv2.resize(face_roi, (450, 450))

                        # Saving to your specific D: drive folder
                        file_name = f"user.{self.var_std_id.get()}.{img_id}.jpg"
                        file_name_path = os.path.join(data_dir, file_name)

                        cv2.imwrite(file_name_path, face_roi)

                        cv2.putText(frame, f"Captured: {img_id}/100", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1,
                                    (0, 255, 0), 2)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                    cv2.imshow("Face Scanner - Press Enter to Exit Early", frame)

                    # Press Enter (13) to break, or wait for 100 samples
                    if cv2.waitKey(1) == 13 or img_id == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", f"Successfully captured 100 samples in:\n{data_dir}", parent=self.root)

            except Exception as e:
                messagebox.showerror("Error", f"Operation Failed: {str(e)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System1(root)
    root.mainloop()