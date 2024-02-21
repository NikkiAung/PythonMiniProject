import math
squareSide = int(input('Enter the side of the square: '))
radius = int(input('Enter the radius of the circle: '))

while (radius*2) != squareSide and (radius*2) > squareSide:
    print('Invalid input')
    radius = int(input('Enter the radius of the circle: '))

excessCardArea = (squareSide**2) - ( math.pi * radius * radius)
print('The excessArea is', excessCardArea)