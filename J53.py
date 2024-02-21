# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
numCoffee = 0  # For counting up
numTea = 0
noDrink = 0
choice = ""  # What the person wants to drink
layout = ""  # For formatting string
drinks = ["T", "T", "C", "T", "C", "T", "T", "C", "T", "C"]

# -------------------------------------------------------------------
# Main program
# ---------------
for i in range(len(drinks)):
    if drinks[i] in 'C':
        numCoffee += 1

    elif drinks[i] in 'T':
        numTea += 1

total = numTea + numCoffee
print('Coffee','    ','Tea','    ','None','    ','Total')
print(36 * '=')
print(' ',numCoffee,'        ',numTea,'      ',noDrink,'       ',total)

print('numTea',numTea)
print('numCoffee',numCoffee)
print('noDrink',noDrink)