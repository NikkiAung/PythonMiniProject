import random

carCounts = []

def genNumbers(pNumberList, pCount):
    index = 0

    for index in range(0, pCount):
        pNumberList.append(random.randint(0,21))



def findMaxCount(pNumberList):
    currentMax = -1
    index = 0

    for index in range(0,len(pNumberList)):
        if (pNumberList[index] > currentMax):
            currentMax = pNumberList[index]

    return (currentMax)

genNumbers(carCounts, 7)

print(carCounts)
print('The maximum count of cars is: ', findMaxCount(carCounts))
