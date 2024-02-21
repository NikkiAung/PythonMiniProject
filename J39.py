firstNames = ["Ashura","Bryn","Eloise","Mei","James","Irene"]
userInput = input('Enter a name to identify the position: ')
if userInput in firstNames:
    print(userInput,'is present in index number', firstNames.index(userInput))
else:
    print(userInput,'is not present in list')



'or'


firstNames = ["Ashura","Bryn","Eloise","Mei","James","Irene"]
userInput = input('Enter a name to identify the position: ')
found = False
index = 0
while not found and index <= (len(firstNames) -1):
    if firstNames[index] == userInput:
        found = True
    index += 1
if found == True:
    print(userInput, 'is present in index number', index)
else:
    print('not found')