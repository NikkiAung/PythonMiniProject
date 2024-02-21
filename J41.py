# Presence check is used to ensure that a value has been entered
# preventing the user from leaving the input blank

userInput = input('Enter a string again: ')
while userInput == '':
    print('Type something!')
    userInput = input('Enter a string again: ')
print('You are good to go!')