upper_limit = int(input('Enter the upper limit: '))
lower_limit = int(input('Enter the lower limit: '))
num = int(input('Enter a number: '))

if lower_limit <= num <= upper_limit:
    print('The number is within the limits.')
else:
    print('The number is not within the limits.')