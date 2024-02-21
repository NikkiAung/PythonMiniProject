nitrateLevel = int(input('Enter a nitrate level between 1 and 50: '))
while nitrateLevel < 1 or nitrateLevel > 50:
    nitrateLevel = int(input('Enter a nitrate level between 1 and 50: '))

if nitrateLevel > 10:
    print('Dose 3 ml')
elif nitrateLevel <= 10 and nitrateLevel > 2.5:
    print('Dose 2 ml')
elif nitrateLevel <= 2.5 and nitrateLevel > 1:
    print('Dose 1 ml')
else:
    print('Dose 0.5 ml')