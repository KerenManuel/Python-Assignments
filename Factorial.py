#Assignment 4
"""This project is the build a python program that print the factorial of a numbers."""


x = int(input("Enter number: "))
if x < 0:
  print("no factorial")
elif x == 0:
  print("Factorial is 1")
else:
 num = 1
for x in range(1,x+1):
    num = num * x
    print(num)





