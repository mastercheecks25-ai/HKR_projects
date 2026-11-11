#This is an updated version of the previous code. 
# It now includes error handling to ensure that the user inputs valid numbers. 
# If the user enters a non-integer value, it will prompt them to enter valid numbers again.
#just for fun
end = True
while end:
    try:
        first_number = input('Enter the first number: ')
        second_number = input('Enter the second number: ')
        first_number = int(first_number)
        second_number = int(second_number)
        if first_number < second_number:
            print('The first number is the smallest.')
            break
        elif first_number > second_number:
            print('The second number is the smallest.')
            break
        elif first_number == second_number:
            print('The numbers are equal.')
            break
    except ValueError:
        print('Please enter valid numbers.')    
