#3. Warehouse Automation System
#Track goods movement, generate inventory reports, and forecast demand.

inventory = {}
movements = {}

while True:
    print("\n===== Warehouse Automation System =====")
    print("1. Add Product")
    print("2. Stock In")
    print("3. Stock Out")
    print("4. Inventory Report")
    print("5. Demand Forecast")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pid = input("Enter Product ID: ")
        pname = input("Enter Product Name: ")
        qty = int(input("Enter Initial Quantity: "))
        
        inventory[pid] = {"Name": pname, "Quantity": qty}
        movements[pid] = []
        print("Product Added Successfully!")

    elif choice == "2":
        pid = input("Enter Product ID: ")
        qty = int(input("Enter Quantity to Add: "))
        
        if pid in inventory:
            inventory[pid]["Quantity"] += qty
            movements[pid].append(qty)
            print("Stock Updated!")
        else:
            print("Product not found")

    elif choice == "3":
        pid = input("Enter Product ID: ")
        qty = int(input("Enter Quantity to Remove: "))
        
        if pid in inventory and inventory[pid]["Quantity"] >= qty:
            inventory[pid]["Quantity"] -= qty
            movements[pid].append(-qty)
            print("Stock Removed!")
        else:
            print("Not enough stock or product not found")

    elif choice == "4":
        print("\n===== Inventory Report =====")
        for pid, data in inventory.items():
            print("ID:", pid, "| Name:", data["Name"], "| Quantity:", data["Quantity"])

    elif choice == "5":
        print("\n===== Demand Forecast =====")
        for pid, move in movements.items():
            if len(move) > 0:
                demand = abs(sum(move)) / len(move)
                print("Product ID:", pid, "Predicted Demand:", int(demand))
            else:
                print("Product ID:", pid, "No movement data")

    elif choice == "6":
        print("Exiting system...")
        break

    else:
        print("Invalid choice")