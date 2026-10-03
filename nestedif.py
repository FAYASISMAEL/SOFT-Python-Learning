num = int(input('Enter a num: '))

if num > 5:
    if num % 2 == 0:
        print(num, ' is a even number.')
    else:
        print(num, ' is a odd number.')
else:
    print(num, ' is less than or equal to 5.')
    