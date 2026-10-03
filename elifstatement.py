# greatest of 3 number.

num1 = int(input('Enter Num1: '))
num2 = int(input('Enter Num2: '))
num3 = int(input('Enter Num3: '))

if num1 > num2:
    great = num1
elif num2 > num3:
    great = num2
else:
    great = num3

print('The greatest number is: ', great)