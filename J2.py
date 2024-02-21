triangleTable = [[22, 33],
                 [11, 66],
                 [66, 99],
                 [44, 88],
                 [99, 55]]

for sides in triangleTable:
    hypotenuse = (sides[0]**2 + sides[1]**2)**(1/2)
    hypotenuse = round (hypotenuse, 1)

    area = (1/2) * sides[0] * sides[1]
print(hypotenuse)
print(area)