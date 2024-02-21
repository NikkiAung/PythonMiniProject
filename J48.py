def calculationMenu():
    print('Here are options below')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')


def workout(firstNum,secondNum,option):
    if option == 1:
        res = firstNum + secondNum
        print('Addition',res)
    elif option == 2:
        res = firstNum - secondNum
        print('Subtraction', res)
    elif option == 3:
        res = firstNum * secondNum
        print('Multiplication', res)
    elif option == 4:
        res = firstNum / secondNum
        print('Division', res)
calculationMenu()

option = int(input('Enter your choice: '))
while option < 1 or option > 4:
    option = int(input('Enter your choice again: '))

firstNum = int(input('Enter your 1st num: '))
secondNum = int(input('Enter your 2nd num: '))

workout(firstNum,secondNum,option)
question = input('Continue : y or n?')
while question == 'y':
    calculationMenu()
    option = int(input('Enter your choice: '))
    while option < 1 or option > 4:
        option = int(input('Enter your choice again: '))

    firstNum = int(input('Enter your 1st num: '))
    secondNum = int(input('Enter your 2nd num: '))

    workout(firstNum, secondNum, option)
    question = input('Continue : y or n?')
else:
    print('Have a good day!')