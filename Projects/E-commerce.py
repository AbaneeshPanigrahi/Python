class InvalidCouponError(Exception):
    pass

class OutOfStockError(Exception):
    pass

class InvalidPaymentError(Exception):
    pass


class ECommerce:

    def __init__(self):
        self.products = {}
        self.orders = []

    def add_product(self):
        try:
            pid = int(input("Enter product ID: "))
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))

            if pid in self.products:
                print("Product ID already exists!")
                return

            self.products[pid] = {
                "name": name,
                "price": price,
                "stock": stock
            }

            print("Product added successfully!")

        except ValueError:
            print("Invalid input! Enter correct values.")

    def show_products(self):
        print("\nAvailable Products")
        for pid, details in self.products.items():
            print(pid, "-", details["name"], "| Price:", details["price"], "| Stock:", details["stock"])

    def place_order(self):
        try:
            self.show_products()

            pid = int(input("Select product number: "))
            quantity = int(input("Enter quantity: "))
            coupon = input("Enter coupon code (press Enter if none): ")
            payment = input("Enter payment method (card/upi/cash): ")

            if pid not in self.products:
                raise OutOfStockError("Product does not exist!")

            product = self.products[pid]

            if quantity > product["stock"]:
                raise OutOfStockError("Product out of stock!")

            total = product["price"] * quantity

            if coupon != "":
                if coupon != "SAVE10":
                    raise InvalidCouponError("Invalid coupon code!")
                total *= 0.9

            if payment not in ["card", "upi", "cash"]:
                raise InvalidPaymentError("Invalid payment method!")

            product["stock"] -= quantity
            self.orders.append(product["name"])

            print("Order placed successfully!")
            print("Total price:", total)

        except (InvalidCouponError, OutOfStockError, InvalidPaymentError) as e:
            print("Error:", e)
        except ValueError:
            print("Invalid input!")

    def return_order(self):
        name = input("Enter product name to return: ")

        if name in self.orders:
            self.orders.remove(name)
            for p in self.products.values():
                if p["name"] == name:
                    p["stock"] += 1
            print("Product returned. Refund initiated.")
        else:
            print("Order not found!")


shop = ECommerce()

while True:
    print("\n--- E-Commerce Order Management ---")
    print("1. Add Product")
    print("2. Show Products")
    print("3. Place Order")
    print("4. Return Order")
    print("5. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            shop.add_product()

        elif choice == 2:
            shop.show_products()

        elif choice == 3:
            shop.place_order()

        elif choice == 4:
            shop.return_order()

        elif choice == 5:
            print("Exiting system")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Enter a valid number!")