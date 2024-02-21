ON_ROLL = 3722
languageTable = ['French','Italian', 'Spanish', 'Mandarin', 'German']
enrolmentNumbers = [366,130,494,79,243]
index = 0
total = 0

for i in range(0,len(enrolmentNumbers)):
    total += enrolmentNumbers[i]
    print(languageTable[i] + ' ' + str(enrolmentNumbers[i]) + ' ' + str(round(100 * enrolmentNumbers[i] / ON_ROLL,2)))
print('The total language is' + ' ' + str(total) + ' ' + str(round(100 * total / ON_ROLL,2)))
