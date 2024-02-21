#range check (between 0 to 100)

userInput = int(input('Enter a val between 0 to 100: '))
while userInput < 0 or userInput > 100:
    print('Invalid')
    userInput = int(input('Enter a val between 0 to 100 again: '))
print('Valid')