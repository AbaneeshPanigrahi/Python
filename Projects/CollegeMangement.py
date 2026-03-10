# College Result Management System

students = {}

while True:
    print("\n--- College Result Management ---")
    print("1. Add Student and Marks")
    print("2. View Results")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        num_subjects = int(input("Enter number of subjects: "))
        marks = []

        for i in range(1, num_subjects + 1):
            while True:
                score = float(input(f"Enter marks for subject {i}: "))
                if 0 <= score <= 100:
                    marks.append(score)
                    break
                else:
                    print("Marks should be between 0 and 100. Try again.")

        students[name] = marks
        print(f"Marks for {name} added successfully!")

    elif choice == 2:
        if not students:
            print("No student data available.")
        for name, marks in students.items():
            total = sum(marks)
            avg = total / len(marks)
            gpa = round(avg / 20, 2)  

          
            if avg >= 95:
                grade = "O"  
            elif avg >= 85:
                grade = "E"  
            elif avg >= 75:
                grade = "A"
            elif avg >= 65:
                grade = "B"
            elif avg >= 55:
                grade = "C"
            elif avg >= 45:
                grade = "D"
            else:
                grade = "F"

            print("\n---------------------------")
            print(f"Student: {name}")
            print("Marks:", marks)
            print("Total:", total)
            print("Average:", round(avg, 2))
            print("GPA (out of 5):", gpa)
            print("Grade:", grade)
            print("---------------------------")

    elif choice == 3:
        print("System Closed")
        break

    else:
        print("Invalid Choice. Try again.")