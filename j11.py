target = 0 # experiment with this value
myArray = [7, 9, 2, 8, 4]  # experiment with the values in the list

arrayLength = len(myArray)
found = False
counter = 0
while counter < arrayLength and not found:
    if myArray[counter] == target:
        print(target, "found at position", str(counter))
        found = True
    else:
        counter += 1
    # endif
# endwhile

if not found:
    print(target, "not found")
# endif
print(counter)


### step-by-step algorithm is shown in the answers to the linear search activity