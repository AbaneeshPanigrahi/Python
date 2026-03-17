import time
import random

class OverdraftError(Exception):
    pass

class InvalidAccountError(Exception):
    pass

class TransactionTimeoutError(Exception):
    pass


class Bank:

    def __init__(self):
        self.accounts = {}

    def create_account(self):
        acc_no = input("Enter account number: ")
        balance = float(input("Enter initial balance: "))
        self.accounts[acc_no] = balance
        print("Account created successfully!")

    def transfer(self):
        try:
            sender = input("Enter sender account number: ")
            receiver = input("Enter receiver account number: ")
            amount = float(input("Enter amount: "))

            if sender not in self.accounts or receiver not in self.accounts:
                raise InvalidAccountError("Incorrect account number!")

            if self.accounts[sender] < amount:
                raise OverdraftError("Insufficient balance!")

            print("Processing transaction...")
            time.sleep(2)

            if random.randint(1,5) == 3:
                raise TransactionTimeoutError("Transaction timeout!")

            self.accounts[sender] -= amount
            self.accounts[receiver] += amount

            print("Transaction successful!")

        except (InvalidAccountError, OverdraftError, TransactionTimeoutError) as e:
            print("Error:", e)

    def show_accounts(self):
        print("\nAccount Details")
        for acc, bal in self.accounts.items():
            print(acc, ":", bal)


bank = Bank()

while True:
    print("\n--- Banking System ---")
    print("1. Create Account")
    print("2. Transfer Money")
    print("3. Show Accounts")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        bank.create_account()

    elif choice == 2:
        bank.transfer()

    elif choice == 3:
        bank.show_accounts()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")