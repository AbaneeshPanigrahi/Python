#EXception Handiling
#Multiple Exception Handling
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num1 / num2
#     print(f"Result: {result}") 
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.") 
# except ValueError:
#     print("Error: Invalid input. Please enter numbers.") 
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")   
#Raising Exceptions 
# class FiveDivisionError(Exception):
#     pass
# try:
#     num = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     if num == 5 or num2 == 5:
#         raise FiveDivisionError("Cannot divide by 5.")
#     result = num / num2
#     print(f"Result: {result}")
# except FiveDivisionError as e:
#     print("Error:", e)
# using constructors to raise exceptions
class FiveDivisionError(Exception):
    def __init__(self, message="Cannot divide by 5."):
        self.message = message
        super().__init__(self.message)
try:
    num = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    if num == 5 or num2 == 5:
        raise FiveDivisionError
    result = num / num2
    print(f"Result: {result}")
except FiveDivisionError as e:
    print("Error:", e)