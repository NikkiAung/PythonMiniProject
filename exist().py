Exist = True

def newUser():
    userName = input('Enter your name: ')

def login():
    login = input('Enter a password: ')

def changePassword():
    change_Password = input('Change your password: ')

def exist():
    Exist = False






print('1. Register as a new user')
print('2. Login.')
print('3. Change your password.')
print('4. Exist.')
while Exist == True:
    choice = int(input('Please select a menu option. '))
    if choice == 1:
        newUser()
    elif choice == 2:
        login()
    elif choice == 3:
        changePassword()
    elif choice == 4:
        exit()

    else:
        print('Incorrect option. Try again.')