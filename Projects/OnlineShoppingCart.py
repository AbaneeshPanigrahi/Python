products = {}
cart = {}
orders = {}

while True:
    print("\nOnline Shopping Cart System")
    print("1. Add Product")
    print("2. View Products")
    print("3. Add to Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. View Orders")
    print("7. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        pid = input("Product ID: ")
        name = input("Product Name: ")
        price = float(input("Product Price: "))
        products[pid] = {"name": name, "price": price}
        print("Product added successfully.")

    elif ch == "2":
        print("\nAvailable Products:")
        if not products:
            print("No products available.")
        else:
            for pid, details in products.items():
                print(f"{pid} - {details['name']} - ₹{details['price']}")

    elif ch == "3":
        pid = input("Enter Product ID: ")
        qty = int(input("Enter Quantity: "))
        if pid in products:
            cart.setdefault(pid, 0)
            cart[pid] += qty
            print("Product added to cart.")
        else:
            print("Invalid Product ID.")

    elif ch == "4":
        print("\nYour Cart:")
        total = 0
        if not cart:
            print("Cart is empty.")
        else:
            for pid, qty in cart.items():
                name = products[pid]["name"]
                price = products[pid]["price"]
                subtotal = price * qty
                total += subtotal
                print(f"{name} - Qty: {qty} - Subtotal: ₹{subtotal}")
            print(f"Total Amount: ₹{total}")

    elif ch == "5":
        if not cart:
            print("Cart is empty. Cannot checkout.")
        else:
            total = 0
            for pid, qty in cart.items():
                total += products[pid]["price"] * qty

            order_id = len(orders) + 1
            orders[order_id] = {"items": cart.copy(), "total": total}
            cart.clear()
            print(f"Order placed successfully! Order ID: {order_id}")
            print(f"Total Paid: ₹{total}")

    elif ch == "6":
        print("\nOrder History:")
        if not orders:
            print("No orders placed.")
        else:
            for oid, details in orders.items():
                print(f"\nOrder ID: {oid}")
                print(f"Total: ₹{details['total']}")
                print("Items:")
                for pid, qty in details["items"].items():
                    print(f"  {products[pid]['name']} - Qty: {qty}")

    elif ch == "7":
        print("Thank you for shopping with us!")
        break

    else:
        print("Invalid choice.")