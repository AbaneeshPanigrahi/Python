# Variables
# Variables are containers for storing data values.

# Creating Variables
# Python has no command for declaring a variable.

# A variable is created the moment you first assign a value to it.

x = 5
y = "John"
print(x)
print(y)

# Casting
# If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Get the Type
# You can get the data type of a variable with the type() function.

x = 5
y = "John"
print(type(x))
print(type(y))

# Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

# Rules for Python variables:

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

# Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Multi Words Variable Names
# Variable names with more than one word can be difficult to read.

# There are several techniques you can use to make them more readable:

# Camel Case
# Each word, except the first, starts with a capital letter:

myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:

MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:

my_variable_name = "John"

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

# Unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
# The print() function is often used to output variables.

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# Global Variables
# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)