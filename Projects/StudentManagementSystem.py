
class GradeException(Exception):
    def __init__(self, message="Invalid grade! Grade must be between 0 and 100."):
        super().__init__(message)

students = {}

while True:
    print("\n----- Student Management System -----")
    print("1. Add Student Grade")
    print("2. Update Student Grade")
    print("3. Delete Student")
    print("4. View Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            name = input("Enter student name: ")
            id=input("Enter student ID: ")
            grade = float(input("Enter grade: "))
            if grade < 0 or grade > 100:
                raise GradeException()
            students[name] = grade
            print(f"Grade added for {name}.")
            print(f"Student ID: {id}")

        elif choice == "2":
            id = input("Enter student id to update: ")
            if id not in students:
                print("Student not found.")
            else:
                grade = float(input("Enter new grade: "))
                if grade < 0 or grade > 100:
                    raise GradeException()
                students[id] = grade
                print(f"Grade updated for {id}.")

        elif choice == "3":
            id = input("Enter student id to delete: ")
            if id in students:
                del students[id]
                print(f"{id} deleted.")
            else:
                print("Student not found.")

        elif choice == "4":
            if not students:
                print("No students found.")
            else:
                for id, grade in students.items():
                    print(f"{id}: {grade}")
                    print(f"Student ID: {id}")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print(" Invalid choice. Please try again.")

    except GradeException as ge:
        print(f"Error: {ge}")
    except ValueError:
        print(" Please enter a valid number for grade.")

