#Assignment 2

"""This project is the build a python program that collects user information,evaluates scores,converts weights and provide
feedback based on conditions."""

print("Student Information and Grades")

student_name = str(input("Enter Your Name: "))
score = float(input("Enter Your Score: "))

if 90 <= score <= 100:
   print(f"Hello!{student_name},your score is {score} and your grade is A. Excellent!")

elif  80 <= score <= 89:
    print(f"Hello!{student_name},your score is {score} and your grade is B. Well Done!")

elif  70 <= score <= 79:
    print(f"Hello!{student_name},your score is {score} and your grade is C. Good Job!")

elif  60 <= score <= 69:
    print(f"Hello!{student_name},your score is {score} and your grade is D. Pass")

elif  60 > score:
    print(f"Hello!{student_name},your score is {score} and your grade is F. Fail")

else:
    print("Invalid score: ")

weight = float(input("Enter Your weight: "))
unit = (input("Kilogram or Pound? (Kg or Lb): "))

if unit == "Kg":
   weight = weight * 2.20462
   unit = "Lb"
   print(f"Your weight is: {round(weight, 2)} {unit}")
elif unit == "Lb":
    weight = weight / 2.20462
    unit = "kg"
    print(f"Your weight is: {round(weight, 2)} {unit}")
else:
       print(f" {unit} weight is invalid")



















