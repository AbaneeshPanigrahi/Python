class DuplicateContactError(Exception):
    pass

class EmptyFieldError(Exception):
    pass

class InvalidPhoneError(Exception):
    pass


class ContactBook:

    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        try:
            name = input("Enter Name: ").strip()
            phone = input("Enter Phone Number: ").strip()

            if name == "" or phone == "":
                raise EmptyFieldError("Fields cannot be empty!")

            if not phone.isdigit() or len(phone) != 10:
                raise InvalidPhoneError("Phone number must be 10 digits!")

            if name in self.contacts:
                raise DuplicateContactError("Contact already exists!")

            self.contacts[name] = phone
            print("Contact added successfully!")

        except (EmptyFieldError, InvalidPhoneError, DuplicateContactError) as e:
            print("Error:", e)

    def edit_contact(self):
        try:
            name = input("Enter contact name to edit: ").strip()

            if name not in self.contacts:
                raise KeyError("Contact not found!")

            print("Leave field empty if you don't want to change it.")

            new_name = input("Enter new name: ").strip()
            new_phone = input("Enter new phone number: ").strip()

            if new_phone != "":
                if not new_phone.isdigit() or len(new_phone) != 10:
                    raise InvalidPhoneError("Invalid phone number!")
                self.contacts[name] = new_phone

            if new_name != "":
                if new_name in self.contacts:
                    raise DuplicateContactError("Contact name already exists!")
                self.contacts[new_name] = self.contacts.pop(name)

            print("Contact updated successfully!")

        except (KeyError, InvalidPhoneError, DuplicateContactError) as e:
            print("Error:", e)

    def search_contact(self):
        try:
            name = input("Enter name to search: ").strip()

            if name == "":
                raise EmptyFieldError("Search field cannot be empty!")

            if name not in self.contacts:
                raise KeyError("Contact not found!")

            print("Name:", name)
            print("Phone:", self.contacts[name])

        except (EmptyFieldError, KeyError) as e:
            print("Error:", e)


book = ContactBook()

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Edit Contact")
    print("3. Search Contact")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            book.add_contact()

        elif choice == 2:
            book.edit_contact()

        elif choice == 3:
            book.search_contact()

        elif choice == 4:
            print("Exiting Contact Book")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")