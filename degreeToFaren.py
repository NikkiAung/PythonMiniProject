userChoice = ''
userTemp = 0
convertedTemp = 0.0
layout = ''
def showMenu ():
    print('----Main Menu ---')
    print('A - Convert Celsius to Fahrenheit')
    print('X - Exist program')

def getUserInput():
    userChoice = ''

    while (userChoice == ''):
        userChoice = input('Please make a userChoice')
        userChoice = userChoice.upper()

        if (userChoice != 'A') and (userChoice != 'C'):
            userChoice = ''
            print('Please make a valid userChoice')

    return (userChoice)

def getUserTemperature():
    return (float(input('Please enter a tempertature')))

def celsuiusTOFahrenheit(pTemperature):

    return ((pTemperature* 9 /5 ) + 32)

print('Welcome to the Temperature Conversion Program')

showMenu()

userChoice = getUserInput()

if (userChoice == 'A'):
    print('Celsius to Fahrenheit')
    userTemp = getUserTemperature()
    convertedTemp = celsuiusTOFahrenheit(userTemp)
    layout = 'Oringinal {:<7.2f} C-->F {:<7.2f}'
    print(layout.format(userTemp, convertedTemp))
print('Gooodbye')