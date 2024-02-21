totalFor = 0
totalAgainst = 0
win = 0
lose = 0
draw = 0
anotherTry = 'Y'

layout = 'Total goals for {} and total goals against {}'

while anotherTry == 'Y':
    goalFor = int(input('Enter a goal for: '))
    totalFor += goalFor

    goalAgainst = int(input('Enter a goal against: '))
    totalAgainst += goalAgainst

    if (goalFor > goalAgainst):
        win += 1
    elif (goalAgainst > goalFor):
        lose += 1
    else:
        draw += 1

    anotherTry = input('Would you love to add more: ').upper()
print(layout.format(totalFor, totalAgainst))
print(win)
print(lose)
print(draw)
