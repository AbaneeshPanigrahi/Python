
class OutOfStockError(Exception):
    pass

class InvalidProductIDError(Exception):
    pass

class InvalidQuantityError(Exception):
    pass


class Inventory:

    def __init__(self):
        self.products = {}

    def add_product(self):
        try:
            pid = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            stock = int(input("Enter Stock Quantity: "))

            if stock < 0:
                raise InvalidQuantityError("Quantity cannot be negative!")

            self.products[pid] = {"name": name, "stock": stock}
            print("Product added successfully!")

        except ValueError:
            print("Invalid input!")

        except InvalidQuantityError as e:
            print("Error:", e)

    def sell_product(self):
        try:
            pid = int(input("Enter Product ID: "))
            qty = int(input("Enter quantity to sell: "))

            if pid not in self.products:
                raise InvalidProductIDError("Product ID does not exist!")

            if qty > self.products[pid]["stock"]:
                raise OutOfStockError("Not enough stock available!")

            self.products[pid]["stock"] -= qty
            print("Product sold successfully!")

        except (InvalidProductIDError, OutOfStockError) as e:
            print("Error:", e)

        except ValueError:
            print("Invalid input!")

    def show_products(self):
        print("\nInventory List")
        for pid, details in self.products.items():
            print(pid, "-", details["name"], "| Stock:", details["stock"])


inv = Inventory()

while True:
    print("\n--- Inventory Management System ---")
    print("1. Add Product")
    print("2. Sell Product")
    print("3. Show Products")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            inv.add_product()

        elif choice == 2:
            inv.sell_product()

        elif choice == 3:
            inv.show_products()

        elif choice == 4:
            print("Exiting system")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")