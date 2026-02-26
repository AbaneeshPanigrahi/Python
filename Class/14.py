# Python If Statement
# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.
# If statement:

a = 33
b = 200
if b > a:
  print("b is greater than a")
# In this example we use two variables, a and b, which are used as part of the if statement to test whether b is greater than a. As a is 33, and b is 200, we know that 200 is greater than 33, and so we print to screen that "b is greater than a".

# How If Statements Work
# The if statement evaluates a condition (an expression that results in True or False). If the condition is true, the code block inside the if statement is executed. If the condition is false, the code block is skipped.

# Example
# Checking if a number is positive:

number = 15
if number > 0:
  print("The number is positive")

# Indentation
# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

# Example
# If statement, without indentation (will raise an error):

# a = 33
# b = 200
# if b > a:
# print("b is greater than a") # you will get an error
# Note: You can use spaces or tabs for indentation, but you must use the same amount of indentation for all statements within the same code block.

# Multiple Statements in If Block
# You can have multiple statements inside an if block. All statements must be indented at the same level.

# Example
# Multiple statements in an if block:

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")
# Using Variables in Conditions
# Boolean variables can be used directly in if statements without comparison operators.

# Example
# Using a boolean variable:

is_logged_in = True
if is_logged_in:
  print("Welcome back!")
# Python can evaluate many types of values as True or False in an if statement.

# Zero (0), empty strings (""), None, and empty collections are treated as False. Everything else is treated as True.

# This includes positive numbers (5), negative numbers (-3), and any non-empty string (even "False" is treated as True because it's a non-empty string).

# Python Elif Statement
# The Elif Keyword
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

# The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
# In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal".

# Multiple Elif Statements
# You can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true.

# Example
# Testing multiple conditions:

score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
# In this example, the program checks each condition in order. Since score is 75, it prints "Grade: C" (the first condition that evaluates to true).

# How Elif Works
# When you use elif, Python evaluates the conditions from top to bottom. As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.

# Important: Only the first true condition will be executed. Even if multiple conditions are true, Python stops after executing the first matching block.

# Example
# Categorizing age groups:

age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")
# When to Use Elif
# Use elif when you have multiple mutually exclusive conditions to check. This is more efficient than using multiple separate if statements because Python stops checking once it finds a true condition.

# Example
# Day of the week checker:

day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

# Python Else Statement
# The Else Keyword
# The else keyword catches anything which isn't caught by the preceding conditions.

# The else statement is executed when the if condition (and any elif conditions) evaluate to False.

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
# In this example a is greater than b, so the first condition is not true, also the elif condition is not true, so we go to the else condition and print to screen that "a is greater than b".

# Else Without Elif
# You can also have an else without the elif:

# Example
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
# This creates a simple two-way choice: if the condition is true, execute one block; otherwise, execute the else block.

# How Else Works
# The else statement provides a default action when none of the previous conditions are true. Think of it as a "catch-all" for any scenario not covered by your if and elif statements.

# Note: The else statement must come last. You cannot have an elif after an else.

# Example
# Checking even or odd numbers:

number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")
# Complete If-Elif-Else Chain
# You can combine if, elif, and else to create a comprehensive decision-making structure.

# Example
# Temperature classifier:

temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

# Else as Fallback
# The else statement acts as a fallback that executes when none of the preceding conditions are true. This makes it useful for error handling, validation, and providing default values.

# Example
# Validating user input:

username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")


# Python Shorthand If
# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.

# One-line if statement:

a = 5
b = 2
if a > b: print("a is greater than b")

# Note: You still need the colon : after the condition.


# Short Hand If ... Else
# If you have one statement for if and one for else, you can put them on the same line using a conditional expression:

# Example
# One-line if/else that prints a value:

a = 2
b = 330
print("A") if a > b else print("B")

# This is called a conditional expression (sometimes known as a "ternary operator").

# Assign a Value With If ... Else
# You can also use a one-line if/else to choose a value and assign it to a variable:

# Example
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

# The syntax follows this pattern:

# variable = value_if_true if condition else value_if_false
# Multiple Conditions on One Line
# You can chain conditional expressions, but keep it short so it stays readable:

# Example
# One line, three outcomes:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


# Practical Examples
# Ternary operators are particularly useful for simple assignments and return statements.

# Example
# Finding the maximum of two numbers:

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)
# Example
# Setting a default value:

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)
# When to Use Shorthand If
# Shorthand if statements and ternary operators should be used when:

# The condition and actions are simple
# It improves code readability
# You want to make a quick assignment based on a condition
# Important: While shorthand if statements can make code more concise, avoid overusing them for complex conditions. For readability, use regular if-else statements when dealing with multiple lines of code or complex logic.

# Python Logical Operators
# Python Logical Operators
# Logical operators are used to combine conditional statements. Python has three logical operators:

# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true
# The and Operator
# The and keyword is a logical operator, and is used to combine conditional statements. Both conditions must be true for the entire expression to be true.

# Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# The or Operator
# The or keyword is a logical operator, and is used to combine conditional statements. At least one condition must be true for the entire expression to be true.

# Example
# Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
# The not Operator
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement.

# Example
# Test if a is NOT greater than b:

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
# Combining Multiple Operators
# You can combine multiple logical operators in a single expression. Python evaluates not first, then and, then or.

# Example
# Combining and, or, and not:

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")
# Truth Tables
# Understanding how logical operators work with different values:

# and Operator Truth Table
# Condition 1	Condition 2	Result
# True	True	True
# True	False	False
# False	True	False
# False	False	False
# or Operator Truth Table
# Condition 1	Condition 2	Result
# True	True	True
# True	False	True
# False	True	True
# False	False	False
# Using Parentheses for Clarity
# When combining multiple logical operators, use parentheses to make your intentions clear and control the order of evaluation.

# Example
# Using parentheses for complex conditions:

# temperature = 25
# is_raining = False
# is_weekend = True

# if (temperature > 20 and not is_raining) or is_weekend:
#   print("Great day for outdoor activities!")
# More Examples
# Example
# User authentication check:

# username = "Tobias"
# password = "secret123"
# is_verified = True

# if username and password and is_verified:
#   print("Login successful")
# else:
#   print("Login failed")
# Example
# Range checking with logical operators:

# score = 85

# if score >= 0 and score <= 100:
#   print("Valid score")
# else:
#   print("Invalid score")

# Python Nested If
# Nested If Statements
# You can have if statements inside if statements. This is called nested if statements.

# x = 41

# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")
# In this example, the inner if statement only runs if the outer condition (x > 10) is true.


# How Nested If Works
# Each level of nesting creates a deeper level of decision-making. The code evaluates from the outermost condition inward.

# Example
# Checking multiple conditions with nesting:

# age = 25
# has_license = True

# if age >= 18:
#   if has_license:
#     print("You can drive")
#   else:
#     print("You need a license")
# else:
#   print("You are too young to drive")
# Multiple Levels of Nesting
# You can nest as many levels deep as needed, but keep in mind that too many levels can make code harder to read.

# Example
# Three levels of nesting:

# score = 85
# attendance = 90
# submitted = True

# if score >= 60:
#   if attendance >= 80:
#     if submitted:
#       print("Pass with good standing")
#     else:
#       print("Pass but missing assignment")
#   else:
#     print("Pass but low attendance")
# else:
#   print("Fail")
# Nested If vs Logical Operators
# Sometimes nested if statements can be simplified using logical operators like and. The choice depends on your logic.

# Example
# This nested if:

# temperature = 25
# is_sunny = True

# if temperature > 20:
#   if is_sunny:
#     print("Perfect beach weather!")
# Example
# Could also be written with and:

# temperature = 25
# is_sunny = True

# if temperature > 20 and is_sunny:
#   print("Perfect beach weather!")
# Both approaches produce the same result. Use nested if statements when the inner logic is complex or depends on the outer condition. Use and when both conditions are simple and equally important.


# More Examples
# Example
# Login validation with nested checks:

# username = "Emil"
# password = "python123"
# is_active = True

# if username:
#   if password:
#     if is_active:
#       print("Login successful")
#     else:
#       print("Account is not active")
#   else:
#     print("Password required")
# else:
#   print("Username required")
# Example
# Grade calculation with nested logic:

# score = 92
# extra_credit = 5

# if score >= 90:
#   if extra_credit > 0:
#     print("A+ grade")
#   else:
#     print("A grade")
# elif score >= 80:
#   print("B grade")
# else:
#   print("C grade or below")


# Python Pass Statement
# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

# a = 33
# b = 200

# if b > a:
#   pass
# The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.


# Why Use pass?
# The pass statement is useful in several situations:

# When you're creating code structure but haven't implemented the logic yet
# When a statement is required syntactically but no action is needed
# As a placeholder for future code during development
# In empty functions or classes that you plan to implement later
# pass in Development
# During development, you might want to sketch out your program structure before implementing the details. The pass statement allows you to do this without syntax errors.

# Example
# Placeholder for future implementation:

# age = 16

# if age < 18:
#   pass # TODO: Add underage logic later
# else:
#   print("Access granted")
# pass vs Comments
# A comment is ignored by Python, but pass is an actual statement that gets executed (though it does nothing). You need pass where Python expects a statement, not just a comment.

# Example
# This will cause an error (empty code block):

# score = 85

# if score > 90:
#   # This is excellent
# # This will raise an IndentationError
# Example
# This works correctly with pass:

# score = 85

# if score > 90:
#   pass # This is excellent
# print("Score processed")

# pass with Multiple Conditions
# You can use pass in any branch of an if-elif-else statement.

# Example
# Using pass in different branches:

# value = 50

# if value < 0:
#   print("Negative value")
# elif value == 0:
#   pass # Zero case - no action needed
# else:
#   print("Positive value")
# pass in Other Contexts
# While we focus on pass with if statements here, it's also commonly used with loops, functions, and classes.

# Example
# Using pass with functions:

# def calculate_discount(price):
#   pass # TODO: Implement discount logic

# # Function exists but doesn't do anything yet