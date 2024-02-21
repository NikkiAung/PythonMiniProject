#Q05FINISHED

libraryRecord =  [
["105MS" , "Marcus" , "Smith" , 25 ],
["103AZ" , "Anthony" , "Zarrent" , 5 ],
["108MW" , "Matt" , "White" , 12 ],
["112DB" , "Denise" , "Bilton" , 58 ],
["124MK" , "Malcolm" , "Kelly" , 86 ],
["116UK" , "Uzere" , "Kevill" , 29 ],
["127AL" , "Abduraheim" , "Leahy" , 94 ],
["124LS" , "Laura" , "Sampras" , 50 ],
["121AP" , "Azra" , "Potter" , 61 ],
["115AC" , "Anthony" , "Calik" , 10 ],
["117PI" , "Pablo" , "Iilyas" , 49 ],
["113MM" , "Mark" , "Montgomerie" , 68 ],
["130FH" , "Felicity" , "Heath" , 11 ],
["132JA" , "Jill" , "Alexander" , 61 ],
["123SG" , "Sara" , "Grimstow" , 9 ],
["134KD" , "Kevin" , "Dawson" , 74 ],
["122AB" , "Andrew" , "Bertwistle" , 42 ],
["125JF" , "Jaide" , "Feehily" , 55 ],
["128JS" , "Justin" , "Slater" , 68 ],
["126CG" , "Colleen" , "Grohl" , 39 ]
]
# ----------------------------------------------
# Write your code below this line
avgNo = 0
totalNo = 0
count = 0
gold = 0
silver = 0
bronze = 0
goldID = 0
silverID = 0
bronzeID = 0

for i in range(0,len(libraryRecord)):

    totalNo += libraryRecord[i][3]
    count += 1
avgNo = totalNo / count


print('The total book readers are', totalNo)
print('The average book readers are', avgNo)
for i in range(0,len(libraryRecord)):
    if libraryRecord[i][3] < 10:
        print(libraryRecord[i][0], 'read fewer than 10 books')
    if libraryRecord[i][3] > gold:
        bronze = silver
        silver = gold
        gold = libraryRecord[i][3]

        goldID = i
    elif libraryRecord[i][3] > silver:
        bronze = silver
        silver = libraryRecord[i][3]

        silverID = i
    elif libraryRecord[i][3] > bronze:
        bronze = libraryRecord[i][3]
        bronzeID = i

print('The gold medal winner is', libraryRecord[goldID][1] + ' ' + libraryRecord[goldID][2], 'with ID number', libraryRecord[goldID][0], 'who reads total of', libraryRecord[goldID][3], 'books')
print('The silver medal winner is', libraryRecord[silverID][1] + ' ' + libraryRecord[silverID][2], 'with ID number', libraryRecord[silverID][0], 'who reads total of', libraryRecord[silverID][3], 'books')
print('The bronze medal winner is', libraryRecord[bronzeID][1] + ' ' + libraryRecord[bronzeID][2], 'with ID number', libraryRecord[bronzeID][0], 'who reads total of', libraryRecord[bronzeID][3], 'books')


