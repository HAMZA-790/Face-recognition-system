import pyodbc
import random

# Connect to database
conn = pyodbc.connect("DRIVER={SQL Server};SERVER=DESKTOP-MJ246J1;DATABASE=face_recognition;Trusted_Connection=yes;")
cursor = conn.cursor()

# Clear existing records
print("Clearing old records...")
cursor.execute("DELETE FROM student")
conn.commit()

# Sample data arrays
names = [
    "hamza iftikhar", "abubbakr imran", "awais mansoor", "arhma ariyan", "hassan habib", 
    "ali ramzan", "hafiz zeeshan", "abudullah ilyas", "abdullah ashraf", "ahmed khan"
]

divisions = ["A", "B", "C", "D", "E"]
teachers = ["mam aqsa sarfraz", "mam zanaib khali", "sir umer irshad", "sir ali haider", "sir talha"]
departments = ["Computer Science", "Software Engineering", "Cyber Security"]
courses = ["BSCS", "BSE", "MCS"]
years = ["2022", "2023", "2024"]
semesters = ["2", "4", "6"]
dobs = ["12/05/2001", "08/11/2002", "23/02/2000", "15/09/2003", "04/07/2001"]

print("Seeding new students...")

for i, name in enumerate(names):
    s_id = str(i + 1)
    dep = random.choice(departments)
    course = random.choice(courses)
    year = random.choice(years)
    sem = random.choice(semesters)
    div = random.choice(divisions)
    roll = str(1000 + i + 1)
    gender = "Male"
    dob = random.choice(dobs)
    email = f"{name.split()[0]}@example.com"
    phone = f"0300{random.randint(1000000, 9999999)}"
    address = "Lahore, Pakistan"
    teacher = random.choice(teachers)
    photo = "No"

    cursor.execute("INSERT INTO student VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
        dep, course, year, sem, s_id, name.upper(), div, roll, gender, dob, email, phone, address, teacher, photo
    ))

conn.commit()
conn.close()
print("Database seeded perfectly with 10 records!")
