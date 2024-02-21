binaryNum = []
for i in range(0,8):
    bit = int(input('Enter a bit 0 or 1: '))
    binaryNum.append(bit)
print(binaryNum)
denaryNum = (binaryNum[0] * 2**7) +  (binaryNum[1] * 2**6) +  (binaryNum[2] * 2**5) +  (binaryNum[3] * 2**4) +  (binaryNum[4] * 2**3) +  (binaryNum[5] * 2**2) +  (binaryNum[6] * 2**1) +  (binaryNum[7] * 2**0)
print(denaryNum)


'''or'''

valid = False
while valid == False:
    incorrectDigit = 0
    numberDigit = 0
    binaryNumber = input('Enter binary number 1 or 0: ')
    if len(binaryNumber) != 8:
        incorrectDigit = 1
    if incorrectDigit == 1:
        print('The digit number length should be 8')
    for index in range(0,len(binaryNumber)):
        if binaryNumber[index] != '0' and binaryNumber[index] != '1':
            numberDigit = 1
    if numberDigit == 1:
        print('All number should be 1 or 0')
    if incorrectDigit == 0 and numberDigit == 0:
        valid = True
print('Binary number is', str(binaryNumber))
convertion = [128,64,32,16,8,4,2,1]
denary = 0
for index in range(0,len(binaryNumber)):
    denary += int(binaryNumber[index]) * convertion[index]
print(denary)