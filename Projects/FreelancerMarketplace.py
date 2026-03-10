#2.Freelancer Marketplace Simulation
#Register freelancers and clients, assign projects, and process payments.
freelancers = {}
clients = {}
projects = {}
payments = {}

while True:
    print("\n===== Freelancer Marketplace =====")
    print("1. Register Freelancer")
    print("2. Register Client")
    print("3. Create Project")
    print("4. Assign Project")
    print("5. Process Payment")
    print("6. View Freelancers")
    print("7. View Clients")
    print("8. View Projects")
    print("9. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        fid = input("Enter Freelancer ID: ")
        name = input("Enter Freelancer Name: ")
        skill = input("Enter Skill: ")
        freelancers[fid] = {"Name": name, "Skill": skill}
        print("Freelancer Registered!")

    elif choice == "2":
        cid = input("Enter Client ID: ")
        name = input("Enter Client Name: ")
        clients[cid] = {"Name": name}
        print("Client Registered!")

    elif choice == "3":
        pid = input("Enter Project ID: ")
        pname = input("Enter Project Name: ")
        budget = float(input("Enter Budget: "))
        projects[pid] = {"Project": pname, "Budget": budget, "Freelancer": None}
        print("Project Created!")

    elif choice == "4":
        pid = input("Enter Project ID: ")
        fid = input("Enter Freelancer ID: ")

        if pid in projects and fid in freelancers:
            projects[pid]["Freelancer"] = fid
            print("Project Assigned!")
        else:
            print("Invalid Project or Freelancer ID")

    elif choice == "5":
        pid = input("Enter Project ID: ")

        if pid in projects and projects[pid]["Freelancer"] != None:
            amount = projects[pid]["Budget"]
            payments[pid] = amount
            print("Payment of", amount, "processed for project", pid)
        else:
            print("Project not assigned!")

    elif choice == "6":
        print("\nFreelancers List")
        for fid, data in freelancers.items():
            print(fid, data)

    elif choice == "7":
        print("\nClients List")
        for cid, data in clients.items():
            print(cid, data)

    elif choice == "8":
        print("\nProjects List")
        for pid, data in projects.items():
            print(pid, data)

    elif choice == "9":
        print("Exiting Program")
        break

    else:
        print("Invalid Choice")