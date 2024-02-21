users = [['Aisha', 'password1'],['Ishtar', 'password2'],['Latif', 'password3'],['Nazim', 'password4']]
userName = str(input('Enter your name: '))
found_name = 0
valid = False
while not valid:
    for i in range(len(users)):
        if users[i][0] == userName:
            found_name = 1
            userPass = input('Enter your passowrd: ')
            ID = i
            if users[ID][1] == userPass:
                print('Pass is correct!')
                valid = True
            else:
                print('Pass is not correct!')
                valid = False
    if found_name != 1:
        print('User not regonised')
        valid = False
        break