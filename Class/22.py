#practice questions 
# 1. Write a program that takes two integers, computes their sum, difference, product, and 
# division, checks if they’re even/odd, and converts one to a float. 
"""
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)
if num1 % 2 == 0:
    print(num1, "is even")
else:
    print(num1, "is odd")
if num2 % 2 == 0:
    print(num2, "is even")
else:
    print(num2, "is odd")
float_num1 = float(num1)
print("First integer as float:", float_num1)
float_num2 = float(num2)
print("Second integer as float:", float_num2)

output:
Enter first integer: 12
Enter second integer: 10
Sum: 22
Difference: 2
Product: 120
Division: 1.2
12 is even
10 is even
First integer as float: 12.0
Second integer as float: 10.0
"""
#2. Process a user-entered sentence: count vowels/consonants, reverse it, replace spaces with 
#underscores, capitalize words. 
"""
Sentance=input("Enter a sentence: ")
vowels="aeiouAEIOU"
vowels_count=0
consonants_count=0
for char in Sentance:
    if char in vowels:
        vowels_count+=1
    elif char.isalpha():
        consonants_count+=1
print("Vowels:", vowels_count)
print("Consonants:", consonants_count)
reversed_sentence = Sentance[::-1]
print("Reversed sentence:", reversed_sentence)
print("Sentence with underscores:", Sentance.replace(" ", "_"))
print("Capitalized words:", Sentance.title())
output:
Enter a sentence: i am a BOY
Vowels: 4
Consonants: 3
Reversed sentence: YOB a ma i
Sentence with underscores: i_am_a_BOY
Capitalized words: I Am A Boy
"""
# 3. Filter numeric values from a mixed-type tuple, attempt modification (handle error), and 
# concatenate two tuples. 
"""
t = (1, "a", 5, "hello", 20)

nums = [i for i in t if type(i) == int]
print(nums)

try:
    t[0] = 100
except:
    print("Tuple cannot be changed")

t2 = (7, 8)
print(t + t2)

output:
[1, 5, 20]
Tuple cannot be changed
(1, 'a', 5, 'hello', 20, 7, 8)
"""
# 4. Create a student marks dictionary, then add, update, delete entries, and display keys, values, 
# and items. 
"""
d = {"Aman": 80, "Naman": 70}

d["Ravi"] = 90
d["Aman"] = 85
del d["Naman"]

print(d.keys())
print(d.values())
print(d.items())
output:
dict_keys(['Aman', 'Ravi'])
dict_values([85, 90])
dict_items([('Aman', 85), ('Ravi', 90)])
"""
# 5. Sort strings by length, identify palindromes, and replace spaces with hyphens using list 
# comprehension. 
"""
lst = ["madam", "hello world", "level", "python"]

sorted_lst = sorted(lst, key=len)
print(sorted_lst)

pal = [i for i in lst if i == i[::-1]]
print(pal)

rep = [i.replace(" ", "-") for i in lst]
print(rep)
output:
['level', 'madam', 'python', 'hello world']
['madam', 'level']
['madam', 'hello-world', 'level', 'python']

"""

# 6. Convert a mixed-type tuple to a list, remove integers less than 10, and convert back to a 
# tuple. 
"""
t = (5, 12, 3, 25, 8)

l = list(t)
l = [i for i in l if not (type(i)==int and i<10)]
t = tuple(l)

print(t)
output:
(12, 25)
"""
# 7. Build a Student Record System using nested dictionaries/lists to add students, update marks, 
# compute averages, and find toppers.
""" 
students = {}

students["Aman"] = [80, 90]
students["Naman"] = [70, 60]

students["Aman"][0] = 85

for s in students:
    avg = sum(students[s]) / len(students[s])
    print(s, avg)

top = max(students, key=lambda x: sum(students[x]))
print("Topper:", top)
output:
Aman 87.5
Naman 65.0
Topper: Aman
"""
# 8. Create a contact book using a dictionary with options to add, search, delete, and list contacts. 
"""
contacts = {}

while True:
    ch = input("1.Add 2.Search 3.Delete 4.Show 0.Exit: ")

    if ch == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif ch == "2":
        name = input("Search: ")
        print(contacts.get(name, "Not found"))

    elif ch == "3":
        name = input("Delete: ")
        contacts.pop(name, None)

    elif ch == "4":
        print(contacts)

    elif ch == "0":
        break
        
output:
1.Add 2.Search 3.Delete 4.Show 0.Exit: 1
Name: Aman
Phone: 1234567890
1.Add 2.Search 3.Delete 4.Show 0.Exit: 1
Name: Naman
Phone: 9876543210
1.Add 2.Search 3.Delete 4.Show 0.Exit: 4
{'Aman': '1234567890', 'Naman': '9876543210'}
1.Add 2.Search 3.Delete 4.Show 0.Exit: 2
Search: Aman
1234567890
1.Add 2.Search 3.Delete 4.Show 0.Exit: 3
Delete: Naman
1.Add 2.Search 3.Delete 4.Show 0.Exit
4
{'Aman': '1234567890'}

"""
# 9. Employee Attendance System 
# Build a loop-based menu system to add, remove, and display employee names stored in a 
# dictionary. Use conditions and loops to control program flow. 
"""
emp = {}

while True:
    ch = input("1.Add 2.Remove 3.Show 0.Exit: ")

    if ch == "1":
        name = input("Name: ")
        emp[name] = "Present"

    elif ch == "2":
        name = input("Remove: ")
        emp.pop(name, None)

    elif ch == "3":
        print(emp)

    elif ch == "0":
        break
        
output:
1.Add 2.Remove 3.Show 0.Exit: 1
Name: Aman
1.Add 2.Remove 3.Show 0.Exit: 1
Name: Naman
1.Add 2.Remove 3.Show 0.Exit: 3
{'Aman': 'Present', 'Naman': 'Present'}
1.Add 2.Remove 3.Show 0.Exit: 2
Remove: Naman
1.Add 2.Remove 3.Show 0.Exit: 3
{'Aman': 'Present'}
1.Add 2.Remove 3.Show 0.Exit: 0
"""
# 10. Student Record Manager 
# Create a system where a user can enter multiple student records (name, roll number, marks). 
# Use loops to add records and conditions to filter students based on pass/fail criteria. Store data 
# using dictionaries and lists. 
"""
students = []

n = int(input("Enter number: "))

for i in range(n):
    name = input("Name: ")
    roll = input("Roll: ")
    marks = int(input("Marks: "))
    students.append({"name": name, "roll": roll, "marks": marks})

for s in students:
    if s["marks"] >= 40:
        print("Pass:", s)
    else:
        print("Fail:", s)
output:
Enter number: 2
Name: alex  
Roll: 1
Marks: 78
Name: lex
Roll: 2
Marks: 67
Pass: {'name': 'alex', 'roll': '1', 'marks': 78}
Pass: {'name': 'lex', 'roll': '2', 'marks': 67}"""
# 11. Restaurant Billing System 
# Display a menu with prices and allow users to order multiple items. Calculate the total bill with 
# tax. Use loops for ordering, dictionaries for storing menu, and conditionals for bill logic. 
"""
menu = {}

n = int(input("How many items to add in menu: "))

for i in range(n):
    item = input("Enter item name: ")
    price = int(input("Enter price: "))
    menu[item] = price

print("\nMenu:", menu)

total = 0

while True:
    item = input("Enter item to order (or exit): ")

    if item == "exit":
        break

    if item in menu:
        qty = int(input("Enter quantity: "))
        total += menu[item] * qty
    else:
        print("Item not available")

print("Total:", total)
print("Final Bill:", total + total*0.1)
output:
How many items to add in menu: 2
Enter item name: Burger
Enter price: 50
Enter item name: Pizza
Enter price: 100
Menu: {'Burger': 50, 'Pizza': 100}
Enter item to order (or exit): Burger
Enter quantity: 2
Enter item to order (or exit): Pizza
Enter quantity: 1
Enter item to order (or exit): exit
Total: 200
Final Bill: 220.0
"""