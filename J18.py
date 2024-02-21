def sumNum(list):
    total = 0
    for i in range(len(list)):
        total += list[i]
    print(total)




list = [8, 2, 3, 0, 7]
sumNum(list)



'or'

#withFunction
def sumNum(list):
    total = 0
    total = sum(list)
    print(total)




list = [8, 2, 3, 0, 7]
sumNum(list)