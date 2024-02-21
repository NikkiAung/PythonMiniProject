validChar = False
userChar = '1'

while not validChar:
    userChar = input('Enter a lower or upper case letter: ')

    if ((userChar >= 'a' and userChar <= 'z')) or ((userChar >= 'A') and (userChar <= 'Z')):
        validChar = True

    else:
        print('Invalid input, try gain')

print('You enter' + ' ' + userChar)