list = []
otherCha = []
def vowelFinding(userInput):
    count = 0
    count_ = 0
    for x in userInput:
        if x.lower() in 'a':
            count += 1
            list.append(x)
        elif x.lower() in 'e':
            count += 1
            list.append(x)
        elif x.lower() in 'i':
            count += 1
            list.append(x)
        elif x.lower() in 'o':
            count += 1
            list.append(x)
        elif x.lower() in 'u':
            count += 1
            list.append(x)
        else:
            count_ += 1
            otherCha.append(x)
    print('The vowel words are',list, 'with', count)
    print('Other characters are', otherCha,'with',count_)

userInput = input('Enter a string pls: ')
vowelFinding(userInput)




'or '




def count(val):
    vov = 0
    con = 0
    for i in range(len(val)):
        if val[i] in ['a','e','i','o','u']:
            vov += 1
        else:
            con += 1
    print(vov)
    print(con)


x = input('Enter a string: ')
count(x)