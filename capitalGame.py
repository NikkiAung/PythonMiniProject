# Q01

def displayMenu():
    # Completed subprogram that displays the menu
    print("                    Menu               ")
    print("---------------------------------------")
    print("[1] Add player name")
    print("[2] Play guess the capital city")
    print("[3] End game")
    print("---------------------------------------")


def getMenuChoice():
    # Completed subprogram that gets and validates the menu choice
    choices = [1, 2, 3]
    mChoice = 0

    # Menu choice is validated
    while mChoice not in choices:
        mChoice = int(input("Input your menu choice:  "))

    # valid menu option returned to the main menu
    return mChoice


def addPlaerName():
    plyName = input('Enter your name pls: ')
    while plyName == '':
        plyName = input('Enter your name pls: ')
    return plyName

# Add your code to:
# ensure a player name is input
# return the player name to the main menu


def guessCapital():
    # Partially completed subprogram to:
    # display questions
    # check guesses
    # return final score

    # Arrays holding question numbers, countries and their capital cities
    questions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    countries = ["England", "France", "Spain", "Italy", "Germany", "Scotland", "Wales", "United Arab  Emirates",
                 "China"]
    capitals = ["Landon", "Paris", "Madrid", "Rome", "Berlin", "Edinburgh", "Cardiff", "Abu Dhabi", "Beijing"]

    questionCount = 1
    questionScore = 0



    # Add your code here
    while questionCount <= 5:
         valid = False
         qus = -1
         while not valid:
             qus = int(input('Enter a question: '))

             if qus in questions:
                valid = True
                questions.remove(qus)

             else:
                valid = False
                print('Invalid input')








         country = countries[qus - 1]
         capital = capitals[qus - 1]

         userInput = input('What is the capital of' + ' ' + country)
         if userInput == capital:
             print('Well done')
             questionScore += 1
         else:
            print('The', country, 'of the capital is', capital)
         questionCount += 1


    return questionScore




menuChoice = 0
score = 0
playerName = ""

while menuChoice != 3:
    displayMenu()
    menuChoice = getMenuChoice()

    # Add your code to:
    #   call the relevant subprogram is the menu choice is 1 or 2
    #   display the player name and the score if the menu choice is 3
    if menuChoice == 1:
        playerName = addPlaerName()
    elif menuChoice == 2:
        score = guessCapital()
    elif menuChoice == 3:
        print(playerName, score)








