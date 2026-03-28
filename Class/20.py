#Python Database Connectivity (PDBC) is a set of Python modules that provide a standardized way to connect to and interact with databases.
# It allows developers to write database-agnostic code, meaning that the same code can work with different types of databases 
# (e.g., MySQL, PostgreSQL, SQLite) without modification. 
# PDBC provides a consistent interface for executing SQL queries, managing database connections, and handling transactions. 
# It is commonly used in web development, data analysis, and any application that requires
#  interaction with a database.
#SQl-Structured Query Language is a programming language used to manage and manipulate relational databases. It is the standard language for
# interacting with databases and is used to perform various operations such as querying data, inserting new records, updating existing records, 
# and deleting records.

#SQL is used to communicate with a database and is essential for tasks such as data retrieval,
# data manipulation, and database administration. It allows users to create, modify, and query databases efficiently.

#types of Sql commands:
#1. DDL (Data Definition Language): These commands are used to define and manage the structure of the database. 
# Examples include CREATE, ALTER, and DROP.
#2. DML (Data Manipulation Language): These commands are used to manipulate the data within the database.
# Examples include SELECT, INSERT, UPDATE, and DELETE.
#3. DCL (Data Control Language): These commands are used to control access to the database. Examples include GRANT and REVOKE.
#4. TCL (Transaction Control Language): These commands are used to manage transactions in the database. 
# Examples include COMMIT, ROLLBACK, and SAVEPOINT.

#if python case sensitive then sql is also case sensitive.
# However, SQL keywords are typically written in uppercase for readability, but they can be written in
# lowercase or mixed case as well. The case sensitivity of SQL keywords depends on the database system being used.
# For example, in MySQL, SQL keywords are case-insensitive, while in PostgreSQL, they are case-sensitive. 
# It is generally recommended to follow the convention of writing SQL keywords in uppercase for better readability and to avoid confusion.

#why python case Sensitive and sql is not case sensitive?
#Python is case-sensitive because it allows for more flexibility in naming variables, functions, and other identifiers.
# This means that "Variable" and "variable" would be treated as two different identifiers in Python.
#On the other hand, SQL is not case-sensitive because it is designed to be more user-friendly and to allow for easier readability.
# In SQL, keywords and identifiers can be written in uppercase, lowercase

#constraints in SQL are rules that are applied to the columns of a table to ensure data integrity and consistency.
# They define the rules for the data that can be stored in a table and help maintain the accuracy and reliability of the data. 

# Some common types of constraints in SQL include:
#1. NOT NULL: This constraint ensures that a column cannot have a NULL value.
#2. UNIQUE: This constraint ensures that all values in a column are unique and not duplicated.
#3. PRIMARY KEY: This constraint uniquely identifies each record in a table and cannot have NULL
#4. FOREIGN KEY: This constraint establishes a relationship between two tables by referencing the primary key of another table.
#5. CHECK: This constraint ensures that the values in a column meet a specific condition.
#6. DEFAULT: This constraint provides a default value for a column when no value is specified during insertion.

import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="shrinu12")
cur = con.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS giet")
cur.execute("USE giet")

cur.execute("DROP TABLE IF EXISTS student")

cur.execute("CREATE TABLE student(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50),address VARCHAR(50),desig VARCHAR(50),salary FLOAT,gender VARCHAR(10))")

cur.execute("INSERT INTO student(name,address,desig,salary,gender) VALUES \
('Aman','Delhi','Student',20000,'Male'),\
('Naman','Raipur','Student',25000,'Male'),\
('Anu','Delhi','Teacher',30000,'Female'),\
('Ravi','Raipur','Doctor',15000,'Male'),\
('Sita','Delhi','Teacher',18000,'Female')")

con.commit()

print("T1")

cur.execute("SELECT * FROM student"); print(cur.fetchall())
cur.execute("SELECT name FROM student"); print(cur.fetchall())
cur.execute("SELECT name,address FROM student"); print(cur.fetchall())
cur.execute("SELECT name,salary FROM student"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE name='Aman'"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE address='Delhi'"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE gender='Male'"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE desig='Doctor'"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE salary=15000"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE salary>20000"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE salary<30000"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE gender='Male' AND salary>20000"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE gender='Female' OR address='Raipur'"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE name LIKE 'a%'"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE name LIKE '%h'"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE address LIKE '%pur%'"); print(cur.fetchall())
cur.execute("SELECT * FROM student ORDER BY name ASC"); print(cur.fetchall())
cur.execute("SELECT * FROM student ORDER BY salary DESC"); print(cur.fetchall())
cur.execute("SELECT COUNT(*) FROM student"); print(cur.fetchone())
cur.execute("SELECT COUNT(*) FROM student WHERE gender='Male'"); print(cur.fetchone())

print("T2")

cur.execute("SELECT * FROM student WHERE salary BETWEEN 15000 AND 30000"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE address!='Delhi'"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE desig!='Teacher'"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE name='Aman' OR name='Naman'"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE name LIKE '%a%a%'"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE LENGTH(name)=5"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE address LIKE 'r%'"); print(cur.fetchall())
cur.execute("SELECT * FROM student ORDER BY salary DESC LIMIT 3"); print(cur.fetchall())
cur.execute("SELECT * FROM student ORDER BY salary ASC LIMIT 1"); print(cur.fetchall())
cur.execute("SELECT SUM(salary) FROM student WHERE gender='Male'"); print(cur.fetchone())
cur.execute("SELECT AVG(salary) FROM student WHERE gender='Female'"); print(cur.fetchone())
cur.execute("SELECT COUNT(*) FROM student WHERE salary>20000"); print(cur.fetchone())
cur.execute("SELECT desig,COUNT(*) FROM student GROUP BY desig"); print(cur.fetchall())
cur.execute("SELECT gender,AVG(salary) FROM student GROUP BY gender"); print(cur.fetchall())
cur.execute("SELECT address,SUM(salary) FROM student GROUP BY address"); print(cur.fetchall())
cur.execute("SELECT desig,AVG(salary) FROM student GROUP BY desig HAVING AVG(salary)>20000"); print(cur.fetchall())
cur.execute("SELECT address,COUNT(*) FROM student GROUP BY address HAVING COUNT(*)>1"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE salary>(SELECT AVG(salary) FROM student)"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE salary=(SELECT MAX(salary) FROM student)"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE salary=(SELECT MIN(salary) FROM student)"); print(cur.fetchall())

print("T3")

cur.execute("SELECT DISTINCT salary FROM student ORDER BY salary DESC LIMIT 1 OFFSET 1"); print(cur.fetchall())
cur.execute("SELECT DISTINCT salary FROM student ORDER BY salary DESC LIMIT 1 OFFSET 2"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE salary=(SELECT DISTINCT salary FROM student ORDER BY salary DESC LIMIT 1 OFFSET 1)"); print(cur.fetchall())
cur.execute("SELECT * FROM student s WHERE salary>(SELECT AVG(salary) FROM student WHERE address=s.address)"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE salary IN (SELECT salary FROM student GROUP BY salary HAVING COUNT(*)>1)"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE salary IN (SELECT salary FROM student GROUP BY salary HAVING COUNT(*)=1)"); print(cur.fetchall())
cur.execute("SELECT desig,MAX(salary) FROM student GROUP BY desig"); print(cur.fetchall())
cur.execute("SELECT * FROM student s WHERE salary=(SELECT DISTINCT salary FROM student WHERE desig=s.desig ORDER BY salary DESC LIMIT 1 OFFSET 1)"); print(cur.fetchall())
cur.execute("SELECT * FROM student s WHERE salary>(SELECT AVG(salary) FROM student WHERE desig=s.desig)"); print(cur.fetchall())
cur.execute("SELECT SUM(salary) FROM (SELECT salary FROM student ORDER BY salary DESC LIMIT 3) AS t"); print(cur.fetchone())
cur.execute("SELECT * FROM student s WHERE 1=(SELECT COUNT(*) FROM student WHERE address=s.address)"); print(cur.fetchall())
cur.execute("SELECT desig FROM student GROUP BY desig ORDER BY COUNT(*) DESC LIMIT 1"); print(cur.fetchall())
cur.execute("SELECT address FROM student GROUP BY address ORDER BY SUM(salary) DESC LIMIT 1"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE (desig,salary) IN (SELECT desig,salary FROM student GROUP BY desig,salary HAVING COUNT(*)>1)"); print(cur.fetchall())
cur.execute("SELECT * FROM student WHERE salary>(SELECT MAX(salary) FROM student WHERE address='Delhi')"); print(cur.fetchall())

cur.execute("""
UPDATE student 
SET salary = salary * 1.1 
WHERE salary < (SELECT avg_sal FROM (SELECT AVG(salary) AS avg_sal FROM student) AS t)
""")
con.commit()

cur.execute("""
DELETE FROM student 
WHERE salary < (SELECT min_sal FROM (SELECT MIN(salary) AS min_sal FROM student WHERE desig='Doctor') AS t)
""")
con.commit()

cur.execute("CREATE OR REPLACE VIEW high_salary AS SELECT * FROM student WHERE salary>20000")
cur.execute("CREATE OR REPLACE VIEW city_salary AS SELECT address,SUM(salary) FROM student GROUP BY address")

cur.execute("SELECT name,salary,DENSE_RANK() OVER(ORDER BY salary DESC) FROM student"); print(cur.fetchall())

cur.close()
con.close()
"""
output:
T1
[(1, 'Aman', 'Delhi', 'Student', 20000.0, 'Male'), (2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male'), (3, 'Anu', 'Delhi', 'Teacher', 30000.0, 'Female'), (4, 'Ravi', 'Raipur', 'Doctor', 15000.0, 'Male'), (5, 'Sita', 'Delhi', 'Teacher', 18000.0, 'Female')]
[('Aman',), ('Naman',), ('Anu',), ('Ravi',), ('Sita',)]
[('Aman', 'Delhi'), ('Naman', 'Raipur'), ('Anu', 'Delhi'), ('Ravi', 'Raipur'), ('Sita', 'Delhi')]
[('Aman', 20000.0), ('Naman', 25000.0), ('Anu', 30000.0), ('Ravi', 15000.0), ('Sita', 18000.0)]
[(1, 'Aman', 'Delhi', 'Student', 20000.0, 'Male')]
[(1, 'Aman', 'Delhi', 'Student', 20000.0, 'Male'), (3, 'Anu', 'Delhi', 'Teacher', 30000.0, 'Female'), (5, 'Sita', 'Delhi', 'Teacher', 18000.0, 'Female')]
[(1, 'Aman', 'Delhi', 'Student', 20000.0, 'Male'), (2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male'), (4, 'Ravi', 'Raipur', 'Doctor', 15000.0, 'Male')]
[(4, 'Ravi', 'Raipur', 'Doctor', 15000.0, 'Male')]
[(4, 'Ravi', 'Raipur', 'Doctor', 15000.0, 'Male')]
[(2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male'), (3, 'Anu', 'Delhi', 'Teacher', 30000.0, 'Female')]
[(1, 'Aman', 'Delhi', 'Student', 20000.0, 'Male'), (2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male'), (4, 'Ravi', 'Raipur', 'Doctor', 15000.0, 'Male'), (5, 'Sita', 'Delhi', 'Teacher', 18000.0, 'Female')]
[(2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male')]
[(2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male'), (3, 'Anu', 'Delhi', 'Teacher', 30000.0, 'Female'), (4, 'Ravi', 'Raipur', 'Doctor', 15000.0, 'Male'), (5, 'Sita', 'Delhi', 'Teacher', 18000.0, 'Female')]
[(1, 'Aman', 'Delhi', 'Student', 20000.0, 'Male'), (3, 'Anu', 'Delhi', 'Teacher', 30000.0, 'Female')]
[]
[(2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male'), (4, 'Ravi', 'Raipur', 'Doctor', 15000.0, 'Male')]
[(1, 'Aman', 'Delhi', 'Student', 20000.0, 'Male'), (3, 'Anu', 'Delhi', 'Teacher', 30000.0, 'Female'), (2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male'), (4, 'Ravi', 'Raipur', 'Doctor', 15000.0, 'Male'), (5, 'Sita', 'Delhi', 'Teacher', 18000.0, 'Female')]
[(3, 'Anu', 'Delhi', 'Teacher', 30000.0, 'Female'), (2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male'), (1, 'Aman', 'Delhi', 'Student', 20000.0, 'Male'), (5, 'Sita', 'Delhi', 'Teacher', 18000.0, 'Female'), (4, 'Ravi', 'Raipur', 'Doctor', 15000.0, 'Male')]
(5,)
(3,)
T2
[(1, 'Aman', 'Delhi', 'Student', 20000.0, 'Male'), (2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male'), (3, 'Anu', 'Delhi', 'Teacher', 30000.0, 'Female'), (4, 'Ravi', 'Raipur', 'Doctor', 15000.0, 'Male'), (5, 'Sita', 'Delhi', 'Teacher', 18000.0, 'Female')]
[(2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male'), (4, 'Ravi', 'Raipur', 'Doctor', 15000.0, 'Male')]
[(1, 'Aman', 'Delhi', 'Student', 20000.0, 'Male'), (2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male'), (4, 'Ravi', 'Raipur', 'Doctor', 15000.0, 'Male')]
[(1, 'Aman', 'Delhi', 'Student', 20000.0, 'Male'), (2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male')]
[(1, 'Aman', 'Delhi', 'Student', 20000.0, 'Male'), (2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male')]
[(2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male')]
[(2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male'), (4, 'Ravi', 'Raipur', 'Doctor', 15000.0, 'Male')]
[(3, 'Anu', 'Delhi', 'Teacher', 30000.0, 'Female'), (2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male'), (1, 'Aman', 'Delhi', 'Student', 20000.0, 'Male')]
[(4, 'Ravi', 'Raipur', 'Doctor', 15000.0, 'Male')]
(60000.0,)
(24000.0,)
(2,)
[('Student', 2), ('Teacher', 2), ('Doctor', 1)]
[('Male', 20000.0), ('Female', 24000.0)]
[('Delhi', 68000.0), ('Raipur', 40000.0)]
[('Student', 22500.0), ('Teacher', 24000.0)]
[('Delhi', 3), ('Raipur', 2)]
[(2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male'), (3, 'Anu', 'Delhi', 'Teacher', 30000.0, 'Female')]
[(3, 'Anu', 'Delhi', 'Teacher', 30000.0, 'Female')]
[(4, 'Ravi', 'Raipur', 'Doctor', 15000.0, 'Male')]
T3
[(25000.0,)]
[(20000.0,)]
[(2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male')]
[(2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male'), (3, 'Anu', 'Delhi', 'Teacher', 30000.0, 'Female')]
[]
[(1, 'Aman', 'Delhi', 'Student', 20000.0, 'Male'), (2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male'), (3, 'Anu', 'Delhi', 'Teacher', 30000.0, 'Female'), (4, 'Ravi', 'Raipur', 'Doctor', 15000.0, 'Male'), (5, 'Sita', 'Delhi', 'Teacher', 18000.0, 'Female')]
[('Student', 25000.0), ('Teacher', 30000.0), ('Doctor', 15000.0)]
[(1, 'Aman', 'Delhi', 'Student', 20000.0, 'Male'), (5, 'Sita', 'Delhi', 'Teacher', 18000.0, 'Female')]
[(2, 'Naman', 'Raipur', 'Student', 25000.0, 'Male'), (3, 'Anu', 'Delhi', 'Teacher', 30000.0, 'Female')]
(75000.0,)
[]
[('Student',)]
[('Delhi',)]
[]
[]
[('Anu', 30000.0, 1), ('Naman', 25000.0, 2), ('Aman', 22000.0, 3), ('Sita', 19800.0, 4), ('Ravi', 16500.0, 5)]
"""
