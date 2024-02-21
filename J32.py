perBox = 2.55
boxesNum = int(input('Enter the number of boxes: '))
if boxesNum >= 100:
    pay = boxesNum * perBox * (1-0.2)
    print('20%', pay)
elif boxesNum < 100 and boxesNum >= 75:
    pay = boxesNum * perBox * (1 - 0.15)
    print('15%',pay)
elif boxesNum < 75 and boxesNum >= 50:
    pay = boxesNum * perBox * (1 - 0.10)
    print('10%',pay)
elif boxesNum < 50 and boxesNum >= 25:
    pay = boxesNum * perBox * (1 - 0.05)
    print('5%',pay)
else:
    pay = boxesNum * perBox
    print('No dics',pay)
