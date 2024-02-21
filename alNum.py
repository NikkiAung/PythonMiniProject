FROM_LEN = 4
formName = ''
valid = False

while (not valid):
    formName = input('Enter a form name: ')
    formName.upper()
    if (len(formName) == FROM_LEN):
        if (formName.isalnum()):
            if ((formName[0] == '7') or
                (formName[0] == '8') or
                (formName[0] == '9')):

                if ((formName[1].isalpha) and
                    (formName[1].isalpha) and
                    (formName[1].isalpha)):

                    valid = True
                    print('Your entry is valid', formName)
                else:
                    print('Last 3 nums should be letter.')
            else:
                print('First letter should be nums')
        else:
            print('Your entry is invalid')
    else:
        print('Form name is not correct.')