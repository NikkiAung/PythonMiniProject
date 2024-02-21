def calcu(num1,num2, choice):
    if choice == 1:
        return num1 + num2
    elif choice == 2:
        return num1 - num2
    elif choice == 3:
        return num1 * num2
    elif choice == 4:
        return num1 / num2



num1 = float(input('Enter 1st num: '))
num2 = float(input('Enter 2nd num: '))
choice = int(input('Enter a choice: '))
res = calcu(num1,num2, choice)
print('The calculation is', res)