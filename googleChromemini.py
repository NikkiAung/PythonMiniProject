# Q05

# Array of words
wordArray = ["wind","leer","pushy","lade","size","sob","borrowing","list",
             "perish","hoax","sticks","seed","impel","large","male","silent",
             "quilt","sobbed","remarkable","fantastic","wire","reflective","putrid",
             "pushover","swing"]


# Add your code here
stop = True
count1 = 0
count2 = 0
highest = 0
lowest = 0
list = []
user_input = input('Enter a word or 1 to quit: ')
stop = True
while stop:
    for i in range(0, len(wordArray)):
        if user_input[0:1] == wordArray[i][0:1]:
            print(wordArray[i])
            count1 += 1
    print(count1,'words begin with',user_input[0:1])
    print('-' * 45)

    for i in range(0, len(wordArray)):
        if user_input in wordArray[i]:
            list.append(wordArray[i])
            print(wordArray[i])

            count2 += 1
    print(count2,'words begin with',user_input)

    user_input = input('Enter a word or 1 to quit: ')
    if user_input == '1':
        stop = False
    else:
        stop = True


for x in range(0,len(list)):
    if len(list[x]) > highest:
        highest = len(list[x])
        highestID = x
    else:
        lowestID = x
print('The longest letter among the list is',list[highestID])
print('The shortest letter among the list is',list[lowestID])