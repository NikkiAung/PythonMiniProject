def findingEven(numList):
    evenNum = []
    for i in range(len(numList)):
        if numList[i] % 2 == 0:
            evenNum.append(numList[i])
    print('Even numbers are', evenNum)







numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
findingEven(numList)