addressBook = [['Andrew Smith', 'as@buzz.com'], ['Maddison Jones','madJon@gmool.co.uk'], ['Bert Tintwhistle', 'BTWhistle@vgmail.com'], ['Richard Burton', 'RichBurt@ct.com'], ['Ann Mills', 'ann@mills.co.uk']]


anotherGo = 'y'
while anotherGo == 'y':
    searchName= input('Enter a name: ')
    found = False
    index = 0
    while found == False and index <= (len(addressBook) - 1):
        if addressBook[index][0] == searchName:
            print('The email address of', searchName,'is', addressBook[index][1])
            found = True
        else:
            index += 1

    if found == False:
        print('This contact is not in your address book.')
    anotherGo = input("\n Press 'y' if you want another go.")