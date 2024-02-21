clubTable = [['Drama','Brownn','Tuesday', 24],
             ['Martial Arts','Green', 'Thursday',45],
             ['Computer', 'White', 'Monday',20],
             ['Chess','Black','Thursday',10]]
userChoice = ''
day = ''
club = ''
def displayClubs():
    layout = '{:<20} {:<15} {:<10} {:^7}'
    print(layout.format('Name','Staff','Day','Number'))
    print('_' * 60)

    layout = '{:<20} {:<15} {:<10} {:^7}'
    for club in clubTable:
        print(layout.format(club[0],club[1],club[2],club[3]))


def showMenu():
    key = ''
    invalidKey = True
    while invalidKey:
        print('\n============Menu============')
        print('Please choose from the following')
        print('Add a club')
        print('Display a club')
        print('Find a club')
        print('Quit the program')

        key = input('What is your choice? ')
        key = key.upper()

        if (key != 'A' and key != 'D' and key != 'F' and key != 'Q'):
            invalidKey = True
            print('*** Invalid Key Try Again ***')
        else:
            invalidKey = False

    return key

def addClub():
     name = ''
     staff = ''
     day = ''
     number = 0
     record = []

     name = input('Enter the name of the club')
     staff = input('Enter the last name of the staff in charge')
     day = input('Enter the day the club meets')
     number = int(input('Enter the number of students in the club'))

     record.append(name)
     record.append(staff)
     record.append(day)
     record.append(number)

     clubTable.append(record)

def findAllByDay (pDay):
        inday = ''
        clubDay = ''
        allClubs = []
        inDay = pDay.upper()
        for club in clubTable:
            clubDay = club[2].upper()
            if (clubDay == inDay):
                allClubs.append(club[0])

        return (allClubs)

while (userChoice != 'Q'):
    userChoice = showMenu()

    if (userChoice == 'A'):
        addClub()

    elif (userChoice == 'D'):
        displayClubs()

    elif (userChoice == 'F'):
        day = input('What day would you like to go')

        theClubs = findAllByDay(day)


        if (len(theClubs) != 0):
            for club in theClubs:
                print(club)

        else:
            print('No club meet that day.')

print('Goodbye')