
def bankStatement():

    print('Welcome to National Bank. Enter 1 to see your balance')
    print('2. to deposit money')
    print('3 to withdraw')
    print('4. to exist')



def deposit():
    global totalBalance
    inMoney = int(input('Enter the amount of money you wanna put: '))
    totalBalance += inMoney
    print('User total balance is', totalBalance)

def withdraw():
    global totalBalance
    outMoney = int(input('Enter the amount of money you wanna withdraw: '))
    totalBalance -= outMoney
    print('User total balance is', totalBalance)






totalBalance = 1000
bankStatement()
userInput = int(input('Enter your choice: '))
while userInput < 1 or userInput > 4:
    print('Invalid')
    userInput = int(input('Enter your choice again: '))

if userInput == 1:
    print('Your total balance is', totalBalance)
elif userInput == 2:
    deposit()
elif userInput == 3:
    withdraw()
else:
    print('Thank you for using National Bank')
