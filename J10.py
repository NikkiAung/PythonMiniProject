target = 72  # experiment with different values
myArray = [20, 18, 64, 19, 72, 25, 4]

for item in myArray:
    if item == target:
        print(target, "found")
    # endif
# next item


### step-by-step version
input("\nPress enter to watch the linear search step by step: ")

input("target: " + str(target))
input("myArray: " + str(myArray))
for item in myArray:
    input("\nstart of FOR loop")
    input("comparing " + str(target) + " with " + str(item))
    if item == target:
        input("target (" + str(target) + ") matches item (" + str(item) + ")")
        input(str(target) + " found")
    # endif
# next item