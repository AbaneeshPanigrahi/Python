# Python Indentation
# Indentation refers to the spaces at the beginning of a code line.

# Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

# Python uses indentation to indicate a block of code.

if 24 > 11:
    print("24 is greater than 11")

# The number of spaces is up to you as a programmer, but it has to be at least one.

# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:

# Python Variables
# In Python, variables are created when you assign a value to it:

x = 5
y = "Hello, Kai!"

print(x)
print(y)

# Statements
# A computer program is a list of "instructions" to be "executed" by a computer.

# In a programming language, these programming instructions are called statements.

# In Python, a statement usually ends when the line ends. You do not need to use a semicolon (;) like in many other programming languages (for example, Java or C).

# Semicolons (Optional, Rarely Used)
# Semicolons are optional in Python. You can write multiple statements on one line by separating them with ; but this is rarely used because it makes it hard to read:

# Example
# print("Hello"); print("How are you?"); print("Bye bye!")
# However, if you put two statements on the same line without a separator (newline or ;), Python will give an error:

# Example
# print("Python is fun!") print("Really!")
# Result:

# SyntaxError: invalid syntax