rooms = {}
students = {}
reservations = {}
checkins = {}
payments = {}

while True:
    print("\nHostel Reservation System")
    print("1. Add Student")
    print("2. Add Room")
    print("3. Make Reservation")
    print("4. Check-in Student")
    print("5. Record Payment")
    print("6. View Students")
    print("7. View Rooms")
    print("8. View Reservations")
    print("9. View Check-ins")
    print("10. View Payments")
    print("11. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        sid = input("Student ID: ")
        name = input("Student Name: ")
        students[sid] = name
        print("Student added.")

    elif ch == "2":
        rid = input("Room ID: ")
        rtype = input("Room Type: ")
        rooms[rid] = rtype
        print("Room added.")

    elif ch == "3":
        sid = input("Student ID: ")
        rid = input("Room ID: ")
        if sid in students and rid in rooms:
            reservations.setdefault(sid, set()).add(rid)
            print("Reservation successful.")
        else:
            print("Invalid ID.")

    elif ch == "4":
        sid = input("Student ID: ")
        rid = input("Room ID: ")
        date = input("Check-in Date (YYYY-MM-DD): ")
        if sid in students and rid in rooms:
            checkins.setdefault(sid, {}).setdefault(rid, []).append(date)
            print("Check-in recorded.")
        else:
            print("Invalid ID.")

    elif ch == "5":
        sid = input("Student ID: ")
        rid = input("Room ID: ")
        amount = input("Payment Amount: ")
        if sid in students and rid in rooms:
            payments.setdefault(sid, {})[rid] = amount
            print("Payment recorded.")
        else:
            print("Invalid ID.")

    elif ch == "6":
        print(students)

    elif ch == "7":
        print(rooms)

    elif ch == "8":
        print(reservations)

    elif ch == "9":
        print(checkins)

    elif ch == "10":
        print(payments)

    elif ch == "11":
        break

    else:
        print("Invalid choice.")