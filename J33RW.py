with open('CITY.txt','r') as city:
    count = 1
    outputFile = open('citywWthNo','a')
    for x in city:
        new = str(count) + ' ' + x
        count += 1
        outputFile.write(new)
outputFile.close()