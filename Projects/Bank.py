# Bank Management System 
password = input("Set your Bank Account Password: ")

balance = 0
transactions = []

attempts = 3
while attempts > 0:
    login = input("Enter your password to login: ")
    if login == password:
        print("\nLogin successful!")
        break
    else:
        attempts -= 1
        print(f"Wrong password. Attempts left: {attempts}")

if attempts == 0:
    print("Too many failed attempts. Exiting...")
    exit()

while True:
    print("\n===== Bank Menu =====")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amt = float(input("Enter amount to deposit: "))
        if amt <= 0:
            print("Invalid amount.")
        else:
            balance += amt
            transactions.append(f"Deposit: ₹{amt}")
            print(f"₹{amt} deposited successfully.")

    elif choice == 2:
        amt = float(input("Enter amount to withdraw: "))
        if amt <= 0:
            print("Invalid amount.")
        elif amt > balance:
            print("Insufficient balance.")
        else:
            balance -= amt
            transactions.append(f"Withdraw: ₹{amt}")
            print(f"₹{amt} withdrawn successfully.")

    elif choice == 3:
        print(f"Your current balance is: ₹{balance}")

    elif choice == 4:
        print("\nTransaction History:")
        if not transactions:
            print("No transactions yet.")
        else:
            for t in transactions:
                print(t)

    elif choice == 5:
        print("Thank you for using the Bank Management System.")
        break

    else:
        print("Invalid choice. Please try again.")