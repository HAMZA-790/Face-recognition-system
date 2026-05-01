from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os
import csv

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Details")
        self.root.state('zoomed')

        # ================= VARIABLES =================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # ================= TITLE =================
        title_lbl = Label(self.root, text="STUDENT ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ================= MAIN FRAME =================
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=730)

        # ================= LEFT FRAME =================
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=700)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=5, y=5, width=715, height=300)

        # Labels and Entries
        Label(left_inside_frame, text="Attendance ID", bg="white", font=("times new roman", 11, "bold")).grid(row=0, column=0, padx=10, pady=5, sticky=W)
        Entry(left_inside_frame, textvariable=self.var_atten_id, font=("times new roman", 11), width=20).grid(row=0, column=1, padx=10, pady=5, sticky=W)

        Label(left_inside_frame, text="Roll No", bg="white", font=("times new roman", 11, "bold")).grid(row=0, column=2, padx=10, pady=5, sticky=W)
        Entry(left_inside_frame, textvariable=self.var_atten_roll, font=("times new roman", 11), width=20).grid(row=0, column=3, padx=10, pady=5, sticky=W)

        Label(left_inside_frame, text="Name", bg="white", font=("times new roman", 11, "bold")).grid(row=1, column=0, padx=10, pady=5, sticky=W)
        Entry(left_inside_frame, textvariable=self.var_atten_name, font=("times new roman", 11), width=20).grid(row=1, column=1, padx=10, pady=5, sticky=W)

        Label(left_inside_frame, text="Department", bg="white", font=("times new roman", 11, "bold")).grid(row=1, column=2, padx=10, pady=5, sticky=W)
        Entry(left_inside_frame, textvariable=self.var_atten_dep, font=("times new roman", 11), width=20).grid(row=1, column=3, padx=10, pady=5, sticky=W)

        Label(left_inside_frame, text="Time", bg="white", font=("times new roman", 11, "bold")).grid(row=2, column=0, padx=10, pady=5, sticky=W)
        Entry(left_inside_frame, textvariable=self.var_atten_time, font=("times new roman", 11), width=20).grid(row=2, column=1, padx=10, pady=5, sticky=W)

        Label(left_inside_frame, text="Date", bg="white", font=("times new roman", 11, "bold")).grid(row=2, column=2, padx=10, pady=5, sticky=W)
        Entry(left_inside_frame, textvariable=self.var_atten_date, font=("times new roman", 11), width=20).grid(row=2, column=3, padx=10, pady=5, sticky=W)

        Label(left_inside_frame, text="Attendance Status", bg="white", font=("times new roman", 11, "bold")).grid(row=3, column=0, padx=10, pady=5, sticky=W)
        attendance_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendance, font=("times new roman", 11), state="readonly", width=18)
        attendance_combo["values"] = ("Status", "Present", "Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Buttons Frame
        btn_frame = Frame(left_inside_frame, bg="white", bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=710, height=35)

        btn_config = {"font": ("times new roman", 12, "bold"), "bg": "blue", "fg": "white", "width": 18}
        Button(btn_frame, text="Import csv", command=self.import_csv, **btn_config).grid(row=0, column=0)
        Button(btn_frame, text="Export csv", command=self.export_csv, **btn_config).grid(row=0, column=1)
        Button(btn_frame, text="Update", command=self.update_data, **btn_config).grid(row=0, column=2)
        Button(btn_frame, text="Reset", command=self.reset_data, **btn_config).grid(row=0, column=3)

        # ================= RIGHT FRAME =================
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=760, y=10, width=720, height=700)

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=705, height=660)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll No")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # ================= FUNCTIONS =================
    def fetch_data(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def import_csv(self):
        global mydata
        mydata.clear()
        try:
            fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln) as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                for i in csvread:
                    mydata.append(i)
            self.fetch_data(mydata)
        except Exception as e:
            messagebox.showerror("Error", f"Could not import: {str(e)}", parent=self.root)

    def export_csv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("Error", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", defaultextension=".csv", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported to " + os.path.basename(fln) + " successfully", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Could not export: {str(e)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        if rows:
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")

    def update_data(self):
        # Optional: Save back to the csv if needed. Currently edits the list.
        pass

if __name__ == "__main__":
    mydata = []
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
