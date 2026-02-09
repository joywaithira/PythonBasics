#Create a simple calculator program using python
#first no operator and last number else invalid operator
from selectors import SelectSelector

firstno = float(input("Enter first number:"))

operator = input("Input an operator:")

secondno = float(input("Enter second number:"))

if operator == "+":
    print(firstno + secondno)
elif operator == "-":
    print(firstno - secondno)
elif operator == "*":
    print(firstno * secondno)
elif operator == "/":
    if secondno != 0:
        print(firstno / secondno)
    else :
        print("Cannot divide by zero")

else:
    print("Invalid operator!")










