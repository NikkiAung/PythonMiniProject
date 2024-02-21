capitalL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
smallL = 'abcdefghijklmnopqrstuvwxyz'
specialL = "["'!@$?/{}#%^&*()|,.\<>'"]"
numbers = '1234567890'

capitalL_count = 0
smallL_count = 0
specialL_count = 0
number_count = 0
whiteSpace_count = 0
total = 0
total_mark = 0
markTotal = 5
print('===== Welcome to Password Strength Checker =====')


password = str(input('Enter your password: '))
for x in range(len(password)):
        if password[x] in capitalL:
            capitalL_count += 1


        elif password[x] in smallL:
            smallL_count += 1


        elif password[x] in specialL:
            specialL_count += 1


        elif password[x] in ' ':
            whiteSpace_count += 1


        elif password[x] in numbers:
            number_count += 1

if capitalL_count != 0:
    total_mark += 1
if smallL_count != 0:
    total_mark += 1
if specialL_count != 0:
    total_mark += 1
if whiteSpace_count != 0:
    total_mark += 1
if number_count != 0:
    total_mark += 1



if total_mark == 1:
    print('PasswordScore', total_mark, '/', str(markTotal))
elif total_mark == 2:
    print('PasswordScore', total_mark, '/', str(markTotal))
elif total_mark == 3:
    print('PasswordScore', total_mark, '/', str(markTotal))
elif total_mark == 4:
    print('PasswordScore', total_mark, '/', str(markTotal))
elif total_mark == 5:
    print('PasswordScore', total_mark, '/', str(markTotal))

print('capitalL_count',capitalL_count)
print('small_count',smallL_count)
print('specialL_count',specialL_count)
print('whiteSpace_count',whiteSpace_count)
print('number_count',number_count)

