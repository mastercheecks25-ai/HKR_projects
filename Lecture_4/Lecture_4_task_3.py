guess = int(input('What is 5 + 7? '))
answer = 12
if guess == answer:
    print('Correct!')
elif guess < answer:
    print('Guess too small')
elif guess > answer:
    print('Guess too big')
else:
    print('Error!')