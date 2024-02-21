markList = [80,66,72,90,96,88]
first = 0
second = 0
third = 0
for i in range(0,len(markList)):
    if markList[i] > first:
        third = second
        second = first
        first = markList[i]
    elif markList[i] > second:
        third = second
        second = markList[i]
    elif markList[i] > third:
        third = markList[i]
print(first)
print(second)
print(third)