def binary_search_find(target, arr):
    found = False
    left = 0
    right = len(arr) - 1
    while left <= right and not found:
        middle = (left + right) // 2
        if arr[middle] == target:
            found = True
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
        # endif
    # endwhile
    return found


# end binary_search

letters = ["H", "K", "L", "R", "T", "V", "X"]
letter = "T"  # this can be changed to experiment with different values

print("\nSearching for", letter, ":\n")
in_list = binary_search_find(letter, letters)

if in_list:
    print(letter, "was found in the list.")
else:
    print(letter, "was not found in the list.")
# endif


####### step by step version
input("\n\nPress enter to see the binary sort step by step: ")


def binary_search_find_step(target, arr):
    input("Function about to start")
    input("target recevied as " + str(target) + " and arr received as " + str(arr))
    found = False
    input("found: " + str(found))
    left = 0
    input("left: " + str(left) + " (# first position in array)")
    right = len(arr) - 1
    input("right: " + str(right) + " (# 6th / last position in array calculated as length (7) - 1 = 6)")
    input("\nAbout to enter loop, checking if left < right and not found")
    print("left:", left)
    print("right:", right)
    input("found: " + str(found))
    while left <= right and not found:
        input("\nleft " + str(left) + " <= right " + str(right) + " and found = False")
        input("# Both conditions are true, loop starting: ")
        middle = (left + right) // 2
        input("middle: " + str(middle) + " ( (left " + str(left) + " + right " + str(right) + ") div 2)")
        input("arr[middle]: " + str(arr[middle]))
        input("\nentering IF block")
        if arr[middle] == target:
            print("arr[middle]", arr[middle], "matches target", target)
            input("THEN route followed")
            found = True
            input("found: " + str(found))
        elif arr[middle] < target:
            print("\narr[middle]", arr[middle], "is less than target", target)
            input("ELIF route followed")
            left = middle + 1
            input("left: " + str(left) + " (middle " + str(middle) + " + 1)")
        else:
            print("\narr[middle]", arr[middle], "must be bigger than target", target)
            input("ELSE route followed")
            right = middle - 1
            input("right: " + str(right) + " (middle " + str(middle) + " - 1)")
        # endif
        input("\nEnd of loop, checking if left < right and not found")
        print("left:", left)
        print("right:", right)
        input("found: " + str(found))
    # endwhile
    input("Loop finished")
    input("Returning found: " + str(found))
    return found


# end binarysearch

numbers = [4, 6, 29, 36, 72, 88, 95]
print("letter in list:", numbers)
number = 6  # this can be changed to experiment with different values
print("letter to find:", number)

print("\nSearching for", letter, ":\n")
in_list = binary_search_find_step(letter, letters)

if in_list:
    print(letter, "was found in the list.")
else:
    print(letter, "was not found in the list.")
# endi

