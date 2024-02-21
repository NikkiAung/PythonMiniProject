chicken = 10
sauage = 6
perperoni = 4
pinapple = 7
mushroom = 5
small = 6.95
medium = 8.49
large = 10.49
totalPrice = 0
def menu():
    print('=============','Weclome','==============')
    print('===============','TO','=================')
    print('============',"Freddie's",'=============')
    print('=============','Pizze','================')

    print('At any time when ordering, type "Pricing" to show the pricing' '\n' 'of ingredients and the total cost of your pizza so far.')

def size():
    global totalPrice
    print('And here are general size prices, notes : customize size also accpeted!')
    print('1. small  = $6.95')
    print('2. medium = $8.49')
    print('3. large  = $10.49')
    print('4. Customized Size: Pizze length in inches * with 1')
    pizzaSize_op = int(input('What size pizza would you like, small, medium, larger or custom?'))
    while pizzaSize_op < 1 or pizzaSize_op > 4:
        pizzaSize_op = int(input('Pls make sure what size pizza would you like, small, medium, larger or custom?'))
    if pizzaSize_op == 1:
        totalPrice += small
    elif pizzaSize_op == 2:
        totalPrice += medium
    elif pizzaSize_op == 3:
        totalPrice += large
    elif pizzaSize_op == 4:
        userSizeInput = int(input('Please type the size of your customize pizza in inch length: '))
        res = userSizeInput * 1
        totalPrice += res



def topping():
    print('Here are the topping available for today!')
    print('1. chicken   = $10')
    print('2. sauage    = $6')
    print('3. perperoni = $4')
    print('4. pinapple  = $7')
    print('5. mushroom  = $5')
    global totalPrice
    count = 0
    while count != 3:
        option = int(input('Please select your topping from option (1 to 10) above'))
        while option < 1 or option > 10:
            option = int(input('Please make sure you select your topping from option (1 to 10) above'))
        if option == 1:
            totalPrice += chicken
        elif option == 2:
            totalPrice += sauage
        elif option == 3:
            totalPrice += perperoni
        elif option == 4:
            totalPrice += pinapple
        elif option == 5:
            totalPrice += mushroom
        count += 1



menu()
size()
topping()
userInput = input('Type "Typing" to work out total price')
if userInput == 'Typing':
    print('Your total is', totalPrice,'with $0.32 tax equal to', totalPrice + 0.32)



