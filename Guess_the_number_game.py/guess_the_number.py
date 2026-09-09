secret_number = 4
guess = 0
while guess != secret_number:
    guess = int(input('Guess the number (1-10):'))
    if guess != secret_number:
        print('Wrong , Try again')
    else :
        print('You got it')
