# Look-up check is used to test that a vlaue is one of a predefined of acceptabl

list = [1, 2, 3, 4, 5]
userInput = int(input('Enter a val to identify if its present in the list: '))
while userInput not in list:
    print('It does not exist,so try again!')

    userInput = int(input('Enter a val to identify if its present in the list: '))
print('U r good to go!')