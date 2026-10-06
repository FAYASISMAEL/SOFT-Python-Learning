# Code 
num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
num3 = int(input('Enter 3rd number: '))

if num1 >= num2 and num1 >= num3:
    print('Largest number is: ', num1)

elif num2 >= num1 and num2 >= num3:
    print('Largest number is: ', num2)

else:
    print('largest number is: ', num3)


# Algorithm:-

# Start
# Input three numbers: a, b, and c
# If a >= b and a >= c, then a is the largest
# Else if b >= a and b >= c, then b is the largest
# Else, c is the largest
# Display the largest number
# Stop


# flowchart:-

#         START
#           |
#           v
#    Input a, b, c
#           |
#           v
#   Is a >= b and a >= c?
#        /        \
#      Yes         No
#       |           |
#       v           v
# Largest = a   Is b >= a and b >= c?
#                   /        \
#                 Yes         No
#                  |           |
#                  v           v
#            Largest = b   Largest = c
#                  \          /
#                   \        /
#                    v      v
#                 Display Largest
#                       |
#                       v
#                     STOP