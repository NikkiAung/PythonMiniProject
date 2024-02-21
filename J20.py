#primeNumber
def findingPrimeNumber(userInput):
    for i in range(2,userInput):
        if userInput % i == 0:
            print('Not prime')
            break
    else:
        print('prime')



userInput = int(input('Enter a num: '))
findingPrimeNumber(userInput)