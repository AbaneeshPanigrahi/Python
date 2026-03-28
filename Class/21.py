#Practice
# SECTION A: MCQs 
# 1. What will be the output? 
# x = [1,2,3] 
# print(x * 2) 
# a) [1,2,3,1,2,3] 
# b) Error 
# c) [2,4,6] 
# d) None 
#a)[1, 2, 3, 1, 2, 3]
# 2. What is the output? 
# print(bool("")) 
# a) True 
# b) False 
# c) Error 
# d) None 
#b) False
# 3. Which is mutable? 
# a) tuple 
# b) string 
# c) list 
# d) int 
#c) list
# 4. What will be output? 
# print(10 == 10.0) 
# a) True 
# b) False
# c) Error 
# d) None
#a) True
# SECTION B: Output Prediction 
# 5.  
# a = [1,2,3] 
# b = a 
# b.append(4) 
# print(a) 
#output:[1,2,3,4]
#6. 
# def func(x=[]):
#     x.append(1)
#     return x

# print(func())
# print(func())
#output:
# [1]
#[1, 1]
# 7. 

# for i in range(5):
#     if i == 3:
#         break
#     print(i)
#output:
# 0
# 1 
# 2

# 8. 
# try: 
#     print(10/0) 
# except: 
#     print("Error") 
# finally: 
#     print("Done") 
#output:
# Error
# Done

# SECTION C: Coding Questions 
# 9. Write a program to: - Take input string - Count vowels and consonants 
# string =input("Enter a string: ")
# vowels="aeiouAEIOU"
# vowels_count=0
# consonants_count=0
# for char in string:
#     if char in vowels:
#         vowels_count+=1
#     elif char.isalpha():
#         consonants_count+=1
# print("Number of vowels:",vowels_count)
# print("Number of consonants:",consonants_count)
#output:
# Enter a string: Alexdender Robert william
# Number of vowels: 9
# Number of consonants: 14

# 10. Write a program to: - Read a file - Count number of lines, words and characters 

# 11. Write a program: - Create a class BankAccount - Methods: deposit, withdraw, check balance 
# 12. Write a program: - Accept list of numbers - Remove duplicates 
# - Sort it without using sort() 
# 13. Write a program using lambda + map + filter: - Square only even numbers from list 
# SECTION D: Advanced / Thinking 
# 16. Write a program: - Simulate login system - Use file to store username/password 
# 17. Exception Handling: - Create custom exception "InvalidAgeError" - Raise error if age < 18 
# SECTION E: GUI + Database Based 
# 18. Create a Tkinter form: - Name input - Submit button - Show entered name 
# 19. Python + SQL: - Connect database - Create table Student 
# - Insert 3 records - Fetch and display all 
# 20. Build mini project: 
# STUDENT MANAGEMENT SYSTEM 
# Features: - Add student - View student - Delete student - Store data in file or database

'''
# ===============================
# SECTION A: MCQs (Answers)
# ===============================
# 1 → [1,2,3,1,2,3]
# 2 → False
# 3 → list
# 4 → True


# ===============================
# SECTION B: Output Prediction
# ===============================

a = [1,2,3]
b = a
b.append(4)
print(a)
# Output: [1, 2, 3, 4]

def func(x=[]):
    x.append(1)
    return x

print(func())
print(func())
# Output:
# [1]
# [1, 1]

for i in range(5):
    if i == 3:
        break
    print(i)
# Output:
# 0 1 2

try:
    print(10/0)
except:
    print("Error")
finally:
    print("Done")
# Output:
# Error
# Done


# ===============================
# SECTION C
# ===============================

# 9 Vowels & consonants
s = "Alex"
v = "aeiouAEIOU"
vc = cc = 0
for i in s:
    if i in v:
        vc += 1
    elif i.isalpha():
        cc += 1
print(vc, cc)
# Output: 2 2


# 10 File count
f = open("test.txt","w")
f.write("Hello world\nPython code")
f.close()

f = open("test.txt","r")
data = f.read()
print("Lines:", len(data.split("\n")))
print("Words:", len(data.split()))
print("Chars:", len(data))
f.close()
# Output:
# Lines: 2
# Words: 4
# Chars: 24


# 11 Bank Account
class Bank:
    def __init__(self):
        self.bal = 0
    def deposit(self,x):
        self.bal += x
    def withdraw(self,x):
        if x <= self.bal:
            self.bal -= x
    def show(self):
        print(self.bal)

b = Bank()
b.deposit(1000)
b.withdraw(200)
b.show()
# Output: 800


# 12 Remove duplicates + sort
lst = [3,1,2,3,1]
u = []
for i in lst:
    if i not in u:
        u.append(i)

for i in range(len(u)):
    for j in range(i+1,len(u)):
        if u[i] > u[j]:
            u[i],u[j] = u[j],u[i]

print(u)
# Output: [1, 2, 3]


# 13 lambda + map + filter
lst = [1,2,3,4,5,6]
res = list(map(lambda x:x*x, filter(lambda x:x%2==0,lst)))
print(res)
# Output: [4, 16, 36]


# ===============================
# SECTION D
# ===============================

# 16 Login system
f = open("users.txt","w")
f.write("admin 123\nuser 111")
f.close()

u = "admin"
p = "123"

f = open("users.txt","r")
ok = False
for i in f:
    a,b = i.split()
    if u==a and p==b:
        ok = True
print("Login success" if ok else "Login fail")
f.close()
# Output: Login success


# 17 Custom Exception
class InvalidAgeError(Exception):
    pass

age = 15
try:
    if age < 18:
        raise InvalidAgeError("Invalid Age")
    print("OK")
except InvalidAgeError as e:
    print(e)
# Output: Invalid Age


# ===============================
# SECTION E
# ===============================

# 18 Tkinter (prints in console)
# Run separately if needed


# 19 MySQL
import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="shrinu12")
cur = con.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS db")
cur.execute("USE db")
cur.execute("CREATE TABLE IF NOT EXISTS student(id INT,name VARCHAR(20))")

cur.execute("INSERT INTO student VALUES (1,'Aman'),(2,'Naman'),(3,'Ravi')")
con.commit()

cur.execute("SELECT * FROM student")
print(cur.fetchall())
# Output: [(1,'Aman'), (2,'Naman'), (3,'Ravi')]

cur.close()
con.close()


# 20 Student Management (simple)
import json

data = {}
data["Aman"] = 80
data["Naman"] = 70
print(data)

del data["Naman"]
print(data)
# Output:
# {'Aman': 80, 'Naman': 70}
# {'Aman': 80}
'''
