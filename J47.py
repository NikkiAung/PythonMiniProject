import random
number = random.randint(1,10)
userName = input('Enter your name pls: ')
print('ok',userName,'I am Guessing a number between 1 and 10: ')
userGuess = int(input('What is your guess?: '))
while userGuess != number:
    if userGuess > number:
        print('U guess is too high')
        userGuess = int(input('What is your guess?: '))

    elif userGuess < number:
        print('U guess is too low')
        userGuess = int(input('What is your guess?: '))


print('U guess it correctly.')