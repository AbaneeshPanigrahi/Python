#Event Tracker 
entered_std=set()
rejected_std=set()
while True:
    print("\n1.enter student")
    print("\n2.display")
    print("\n3.exit")
    choice=int(input("enter your choice:"))
    if choice == 1:
        n=int(input("enter no. of students:"))
        print("enter ",n," students name")
        for i in range(n):
            name=input("enter name")
            if name in entered_std:
                print("name already entered. entry rejected")
                rejected_std.add(name)
            else:
                print(name,"entry accepted")
                entered_std.add(name)
    elif choice==2:
        print("entered students are ")
        for i in entered_std:
            print(i)
    elif choice==3:
        break
    else:
        print("invalid input")

print("\n-- Event Report")

print("Entered students : ",entered_std)
print("Rejected students : ",rejected_std)

print("total unique entries : ", len(entered_std))