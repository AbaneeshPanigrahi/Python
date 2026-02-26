
students = {}
courses = {}
enrollments = {}
attendance = {}
grades = {}

while True:
    print("\nStudent Enrollment System")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student")
    print("4. Mark Attendance")
    print("5. Enter Grades")
    print("6. View Students")
    print("7. View Courses")
    print("8. View Enrollments")
    print("9. View Attendance")
    print("10. View Grades")
    print("11. Exit")

    ch = input("Enter choice: ")  

    if ch == "1":
        sid = input("Student ID: ")
        name = input("Student Name: ")
        students[sid] = name
        print("Student added.")

    elif ch == "2":
        cid = input("Course ID: ")
        cname = input("Course Name: ")
        courses[cid] = cname
        print("Course added.")

    elif ch == "3":
        sid = input("Student ID: ")
        cid = input("Course ID: ")
        if sid in students and cid in courses:
            enrollments.setdefault(sid, set()).add(cid)
            print("Enrollment successful.")
        else:
            print("Invalid ID.")

    elif ch == "4":
        sid = input("Student ID: ")
        cid = input("Course ID: ")
        date = input("Date (YYYY-MM-DD): ")
        if sid in students and cid in courses:
            attendance.setdefault(sid, {}).setdefault(cid, []).append(date)
            print("Attendance marked.")
        else:
            print("Invalid ID.")

    elif ch == "5":
        sid = input("Student ID: ")
        cid = input("Course ID: ")
        grade = input("Grade: ")
        if sid in students and cid in courses:
            grades.setdefault(sid, {})[cid] = grade
            print("Grade added.")
        else:
            print("Invalid ID.")

    elif ch == "6":
        print(students)

    elif ch == "7":
        print(courses)

    elif ch == "8":
        print(enrollments)

    elif ch == "9":
        print(attendance)

    elif ch == "10":
        print(grades)

    elif ch == "11":
        break

    else:
        print("Invalid choice.")
