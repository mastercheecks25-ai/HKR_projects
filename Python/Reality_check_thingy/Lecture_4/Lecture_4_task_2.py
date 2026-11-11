while True:
    weather = str(input('Is it sunny outside today(yes/no)? '))
    if weather == 'yes':
        print('I hope it is not too hot outside.')
        break
    elif weather == 'no':
        print('Hopefully the weather will be better tomorrow.')
        break
    else:
        print('Error!')
        