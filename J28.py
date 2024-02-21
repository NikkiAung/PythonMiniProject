def binaryTOdenary(userInput):
    res = 0
    count = 7
    valid = False
    while not valid:
        for x in range(0, len(userInput)):
            if len(userInput) > 8 or len(userInput) < 8 and userInput[x] not in '0' and userInput[x] not in '1':
                valid = False
                userInput = input('Enter the binary number: ')
            else:
                valid = True

        #userInput = input('Enter the binary number: ')
    for x in range(0,len(userInput)):
        res += int(userInput[x]) * 2**count
        count -= 1
    print(res)




userInput = input('Enter the binary number: ')
binaryTOdenary(userInput)