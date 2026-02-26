passwords = {}
strengths = {}

while True:
    print("\nPassword Strength Checker System")
    print("1. Add User Password")
    print("2. Check Password Strength")
    print("3. View Users")
    print("4. View Password Strengths")
    print("5. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        uid = input("Enter User ID: ")
        pwd = input("Enter Password: ")
        passwords[uid] = pwd
        print("Password added.")

    elif ch == "2":
        uid = input("Enter User ID: ")
        if uid in passwords:
            pwd = passwords[uid]

            length = len(pwd) >= 8
            upper = any(c.isupper() for c in pwd)
            lower = any(c.islower() for c in pwd)
            digit = any(c.isdigit() for c in pwd)
            special = any(not c.isalnum() for c in pwd)

            score = sum([length, upper, lower, digit, special])

            if score == 5:
                strength = "Very Strong"
            elif score >= 3:
                strength = "Strong"
            elif score >= 2:
                strength = "Medium"
            else:
                strength = "Weak"

            strengths[uid] = strength
            print(f"Password Strength: {strength}")
        else:
            print("User ID not found.")

    elif ch == "3":
        print(passwords)

    elif ch == "4":
        print(strengths)

    elif ch == "5":
        break

    else:
        print("Invalid choice.")