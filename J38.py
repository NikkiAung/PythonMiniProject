student = [["Smith",1,69],["Jackson",2,45],["John",1,90],["Jackson",1,89],["John",2,70],["Smith",3,90],["Jackson",3,92]]
highMark = 0
middleMark = 0
lowestMark = 0
for i in range(0,len(student)):
    if student[i][1] == 1:
        if student[i][2] > highMark:
            lowestMark = middleMark
            middleMark = highMark
            highMark = student[i][2]
            highID = i
    elif student[i][1] == 2:
        if student[i][2] > middleMark:
            lowestMark = middleMark
            middleMark = student[i][2]
            middleID = i
    elif student[i][1] == 3:
        if student[i][2] > lowestMark:
            lowestMark = student[i][1]
            lowestID = i
print('The highest Mark Acheiver in exam 1 is', student[highID][0], 'with', student[highID][2])
print('The highest Mark Acheiver in exam 2 is', student[middleID][0], 'with', student[middleID][2])
print('The highest Mark Acheiver in exam 3 is', student[lowestID][0], 'with', student[lowestID][2])