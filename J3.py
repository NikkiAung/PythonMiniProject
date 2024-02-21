userTable = [["AAA34", 4860, "chocolate bourbon"],
             ["CAB98", 7101, "custard cream"],
             ["GUS21", 5975, "rich tea"],
             ["RAT67", 4173, "chocolate digestive"],
             ["TUM83", 6462, "shortbread"],
             ["TXA84", 1435, "oatmeal raisin"]]

# =====> Write your code here
#userName = input('Enter your user name: ')
valid = False
while not valid:
    userName = input('Enter your user name: ')
    passWord = int(input('Enter your pass: '))
    favDessert = input('Enter your fav dessert: ')
    for i in (0,len(userTable)):
        if userTable[i][0] == userName and userTable[i][1] == passWord and userTable[i][2] == favDessert:
            valid = True
            print('You are allowed in!')

            break
        else:
            valid = False
            print('Try again!')
            break

