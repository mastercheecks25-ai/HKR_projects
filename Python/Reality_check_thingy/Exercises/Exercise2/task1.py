init_value = 1000

while True:
    withdrawal_amount = int(input('Enter the amount you want to withdraw in 100 sek bills: '))
    if withdrawal_amount % 100 != 0:
        print('Error! Please enter a valid amount in 100 sek bills.')
    elif withdrawal_amount < init_value:
        print('You have withdrawn', withdrawal_amount, 'sek')
        init_value -= withdrawal_amount
        print('Your new balance is', init_value, 'sek')
    elif withdrawal_amount > init_value:
        print('Error! You do not have enough funds to withdraw that amount.')
    else:
        print('Error! Please enter a valid amount.')




    