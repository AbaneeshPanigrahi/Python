#4. CRM (Customer Relationship Manager)
#Store customer info, manage communication logs, and track sales pipelines

customers = {}
communications = {}
sales_pipeline = {}

while True:
    print("\n===== CRM System =====")
    print("1. Add Customer")
    print("2. Add Communication Log")
    print("3. Update Sales Pipeline")
    print("4. View Customers")
    print("5. View Communications")
    print("6. View Sales Pipeline")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        cid = input("Enter Customer ID: ")
        name = input("Enter Customer Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")

        customers[cid] = {
            "Name": name,
            "Email": email,
            "Phone": phone
        }

        communications[cid] = []
        sales_pipeline[cid] = "Lead"

        print("Customer added successfully!")

    elif choice == "2":
        cid = input("Enter Customer ID: ")
        if cid in customers:
            log = input("Enter communication note: ")
            communications[cid].append(log)
            print("Communication recorded!")
        else:
            print("Customer not found")

    elif choice == "3":
        cid = input("Enter Customer ID: ")
        if cid in customers:
            print("Stages: Lead → Contacted → Proposal → Won/Lost")
            stage = input("Enter new stage: ")
            sales_pipeline[cid] = stage
            print("Sales stage updated!")
        else:
            print("Customer not found")

    elif choice == "4":
        print("\n===== Customer List =====")
        for cid, data in customers.items():
            print(cid, data)

    elif choice == "5":
        print("\n===== Communication Logs =====")
        for cid, logs in communications.items():
            print("Customer ID:", cid)
            for l in logs:
                print("-", l)

    elif choice == "6":
        print("\n===== Sales Pipeline =====")
        for cid, stage in sales_pipeline.items():
            print("Customer ID:", cid, "| Stage:", stage)

    elif choice == "7":
        print("Exiting CRM...")
        break

    else:
        print("Invalid choice")