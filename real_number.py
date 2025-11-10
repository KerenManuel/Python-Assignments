#Assignment 3

"""This project is the build a python program that print the first 100 real numbers."""

number = 1 #(where you start from)
while number < 101:
    #print(f"current number: {number}")
    if number % 3 == 0 and number % 5 == 0:
        print("Dr. Fred")
    elif number % 5 == 0:
        print("Stephen")
    elif number % 3 == 0:
        print("Mauricious")
    else:
        print(number)
    number += 1


