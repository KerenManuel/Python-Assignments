# Simple calculator
try:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    c = input("Enter operator:")

    if "+" in c:
      print(a + b)
    elif "-" in c:
      print(a - b)
    elif "*" in c:
      print(a * b)
    elif "/" in c:
      print(a / b)
    elif "%" in c:
      print(a % b)
    input("Press enter to exit:")
except ValueError:
     print("Enter a valid value")
except ZeroDivisionError:
     print("Can not divide by 0")
except ArithmeticError:
     print("Invalid operator")