validChoice = False
userChoice = 0
exitProgram = False

tileColours = ['pink','red','yellow','magenta','purple']
poolDepths = [1.9,2.4,5.6,7.2,9.0]

def showMenu():
    print('Welcome to swimming pool')
    print("_" * 40)
    print('Option-1 add 1 for depth')
    print('Option-2 add 9 for exist')

def doAddDepth():
    depth = 0.0
    depthString = ''

    while depth == 0.0:
        depthString = input('Enter a depth with a decimal: ')

        try:
            depth = float(depthString)

        except:
            print('Invalid input')
            depth = 0.0

        else:
            poolDepths.append(depth)
    print('Depth Added')

while (not validChoice) and (not exitProgram):
    showMenu()
    userChoice = input("Enter your choice")

    if userChoice == '1':
        doAddDepth()
    elif userChoice == '9':
        exitProgram = True
        print(poolDepths)
    else:
        print('Invalid option, try again.')
        validChoice = False

print('GoodBye')
