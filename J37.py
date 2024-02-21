def checkbalance():
    global balance
    print("Your total balance is currently: $", balance )

def deposit():
    global balance
    add = float(input("How much would you like to deposit?: "))
    balance = balance + add

def withdraw():
    global balance
    take = float(input("How much would you like to withdraw?: "))
    balance = balance - take

balance = 875
while True:
    print("\nWelcome to National Bank. Enter 1 to see your balance.")
    print("2 to deposit money")
    print("3 to withdraw")
    print("4 to exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        checkbalance()

    elif choice == 2:
        deposit()

    elif choice == 3:
        withdraw()

    elif choice == 4:
        break

print("Thank you for using National Bank.")
