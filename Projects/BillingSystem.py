#Billing System
#Scan products, apply discounts, generate bills, and record transactions.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_price(self):
        return self.price * self.quantity
class Bill:
    def __init__(self):
        self.items = []
    def add_item(self, product):
        self.items.append(product)
    def calculate_total(self):
        total = sum(item.total_price() for item in self.items)
        return total
    def generate_bill(self):
        print("\n------- BILL -------")
        for item in self.items:
            print(f"{item.name} - {item.quantity} x Rs.{item.price} = Rs.{item.total_price()}")
        print(f"Total Amount: Rs.{self.calculate_total()}")
        print("-------------------")
if __name__ == "__main__":
    bill = Bill()
    while True:
        name = input("Enter product name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        price = float(input("Enter price of the product: "))
        quantity = int(input("Enter quantity: "))
        product = Product(name, price, quantity)
        bill.add_item(product)
    bill.generate_bill()