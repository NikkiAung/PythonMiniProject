#Ab123
Capital_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Small_alphabet   = 'abcdefghijklmnopqrstuvwxyz'
passcode = input('Enter your passcode: ')
if passcode[0] in Capital_alphabet and passcode[1] in Small_alphabet and passcode[2].isdigit() and passcode[3].isdigit() and passcode[4].isdigit():
    print('valid')
elif passcode[0] not in Capital_alphabet and passcode[1] in Small_alphabet and passcode[2].isdigit() and passcode[3].isdigit() and passcode[4].isdigit():
    print('First letter should be capital letter')
elif passcode[0] in Capital_alphabet and passcode[1] not in Small_alphabet and passcode[2].isdigit() and passcode[3].isdigit() and passcode[4].isdigit():
    print('Second letter should be small letter')
elif passcode[0] in Capital_alphabet and passcode[1] in Small_alphabet and not passcode[2].isdigit() and passcode[3].isdigit() and passcode[4].isdigit():
    print('The 3rd letter should be number')
elif passcode[0] in Capital_alphabet and passcode[1] in Small_alphabet and passcode[2].isdigit() and not passcode[3].isdigit() and passcode[4].isdigit():
    print('The 4th letter should be number')
elif passcode[0] in Capital_alphabet and passcode[1] in Small_alphabet and passcode[2].isdigit() and passcode[3].isdigit() and not passcode[4].isdigit():
    print('The 5th letter should be number')