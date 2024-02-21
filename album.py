albumTable = [['Sunshine', 'Met office',2018,True, 12.86, 'Musicals'],
              ['High Rise','Builder Brigade', 2011, False, 23.76, 'Classical'],
              ['Rough Seas', 'Sammy the Sailor', 1996, True, 18.34, 'Folk']]
userChoice = ''
def displayAlnums():
    layout = '{:<15}  {:<20}  {:4} {:^8} {:^9} {:<}'
    print(layout.format('Title','Artist','year','In stock','Price','Genre'))

    #layout = '{:<15}  {:<20}  {:^4} {:^8} {:^9} {:<}'
    for album in albumTable:
        print(layout.format(album[0], album[1], album[2], album[3], album[4], album[5]))

def showMenu():
    key = ''
    invalidKey = True
    while (invalidKey):
        print('\n ===============Menu===================')
        print('Please choose from the following: ')
        print('(A)dd an album')
        print('(D)isplay all the albums')
        print('(Q)uit the program')
        key = input('What is your choice? ')
        key = key.upper()

        if (key != 'A' and key != 'D' and key != 'Q'):
            invalidKey = True
        else:
            invalidKey = False
    return key






def addalbum():
    title = ''
    artist = ''
    year = 0
    inStockString = ''
    inStock = False
    price = 0.0
    genre = ''
    record = []
    title = input('Enter the name of the title: ')
    artist = input('Enter the name of the artist: ')
    year = int(input('Enter the year of the release: '))

    inStockString = input('If in stock, enter Y: ').upper()
    if (inStockString == 'Y'):
        inStock = True
    else:
        inStock = False

    price = float(input('Enter the price: '))
    genre = input('Enter the genre: ')

    record.append(title)
    record.append(artist)
    record.append(year)
    record.append(inStock)
    record.append(price)
    record.append(genre)

    albumTable.append(record)

while (userChoice != 'Q'):
     userChoice = showMenu()

     if (userChoice == 'A'):
         addalbum()
     elif (userChoice == 'D'):
        displayAlnums()
print('Goodbye')


