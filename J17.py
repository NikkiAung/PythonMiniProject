def fac(num):
    fact = 1
    while (num != 0):
        fact *= num
        num = num - 1
    print('Fac is', fact)

num = int(input('Enter a number: '))
fac(num)
