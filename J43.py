#basicLengthWorking!

userString = input('Enter a string: ')
count = 0
for i in userString:
    count += 1
print(count)



'or'
# Length check is used to check the length of a value entered
# within a specified rang

password = input('Enter a password: ')
if len(password) < 7 :
    print('not strong enough')
else:
    print('Strong')