import math
def menu():
    print('_' * 50)
    print('1. Area')
    print('2. Circumference')
    print('3. Exist')

def Area(circleRadius):
    circleRadius = float(input('Enter the circle radius: '))
    area = math.pi * circleRadius**2
    print('The circle area is', area)



def Circumference(circleRadius):
    circleRadius = float(input('Enter the circle radius: '))
    circumference = 2 * math.pi * circleRadius
    print('The circle circumference is', circumference)






menu()
circleRadius = 0
valid = False
while not valid:
    option = int(input('Choose the option number:'))

    if option == 1:
        Area(circleRadius)
        valid = True
    elif option == 2:
        Circumference(circleRadius)
        valid = True
    elif option == 3:
        print('Good bye')
        valid = True
    else:
        valid = False