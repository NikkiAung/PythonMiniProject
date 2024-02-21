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
    player = ''
    while player == '':
        player = input('Enter your name: ')
    return player


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
        questionChoice = -1
        questionNumbers = ''
        for question in questions:
            if question != 0:
                questionNumbers += str(question) + ''
        while str(questionChoice) not in questionNumbers:
            questionChoice = int(input('Pick a number from' + questionNumbers))

        country = countries[questionChoice - 1]
        capital = capitals[questionChoice - 1]

        guess = input('What is the capital of' + country + '?').lower()

        if guess == capital.lower():
            print('Well done!')
            questionScore += 1
        else:
            print('Wrong. The capital of'+ country + 'is' + capital)

        questionCount += 1
        questions[questionChoice - 1] = 0
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
        print(playerName,'gains', score)





















