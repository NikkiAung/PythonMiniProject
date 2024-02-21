theSeason = ''
numMonth = 0
numMonth = int(input('Enter a month no: '))
if numMonth == 12:
    theSeason = 'Winter'
elif numMonth < 12 and numMonth >= 9:
    theSeason = 'Autumn'
elif numMonth < 9 and numMonth >= 6:
    theSeason = 'Summer'
elif numMonth < 6 and numMonth >= 3:
    theSeason = 'Spring'
else:
    theSeason = ''

print('The Season is', theSeason)