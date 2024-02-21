def menu():
    print('What would you like to do?')
    print('1. Add an item to the inventory.')
    print('2. Remove an item from the inventory')



print('Here is your current inventory')
itemList = ['torch','gold coin','key']
menu()
option = int(input('Enter one of the options: '))
if option == 1:
    item = input('Enter an item to add: ')
    itemList.append(item)
else:
    item = input('Enter an item to remove: ')
    itemList.remove(item)

for i in range(len(itemList)):
    print(itemList[i])