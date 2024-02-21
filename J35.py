#1mile=1.609 km
#1inch= 2.54cm

res = 0
def menu():
    print('What conversation would you like to do?')
    print('1. Convert Miles to Kilometres')
    print('2. Convert Kilometres to Miles')
    print('3. Convert CM to Inches')
    print('4. Convert Inches to CM')

def MilesTOKilo(measurement):
    res = measurement * 1.609
    print(measurement,'miles in kilometre is', round(res,1))

def KiloToMiles(measurement):
    res = round(measurement // 1.609,1)
    print(measurement,'kilometres in miles is', res)

def CMToInches(measurement):
    res = measurement // 2.54
    print(measurement,'cm in inches is', round(res,1))

def InchesToCM(measurement):
    res = measurement * 2.54
    print(measurement,'inches in cm is', round(res,1))







menu()
option = int(input('Enter your option from 1 to 4: '))
while option < 1 or option > 4:
    print('Invalid')
    option = int(input('Enter your option from 1 to 4 again: '))

measurement = int(input('Enter your measurement to convert: '))

if option == 1:
    MilesTOKilo(measurement)
elif option == 2:
    KiloToMiles(measurement)
elif option == 3:
    CMToInches(measurement)
elif option == 4:
    InchesToCM(measurement)