def calcHealth(weight, teeth, eyes, ears):
    health = 0
    Multiplier = [50,30,30,10]
    total = 0
    ht = 0
    he = 0
    hr = 0
    hw = 0

    ht = teeth * Multiplier[1]
    he = eyes * Multiplier[2]
    hr = ears * Multiplier[3]
    hw = weight * Multiplier[0]

    total = hw + ht + he + hr
    health = total / 100

    return health

res = calcHealth(5, 5, 5, 5)
print(res)
