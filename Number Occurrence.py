


number_list = input("Enter a list of numbers: ")

given_number = input("Enter given number? ")

position = (number_list.rfind(f'{given_number}'))


print(f'{position + 1}')



n = int(input("Enter a Number: "))
addition = 0
for X in range(1, n//2+1):
    if n%X == 0:
        addition+= X
if addition > n:
    print(f'{n} is an abundant number')
if addition < n:
    print(f'{n} is a deficient number')
if addition == n:
    print(f'{n} is a perfect number')



