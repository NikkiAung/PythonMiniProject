# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# ===>  Change the identifier x to a more meaningful name
ans = ""
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# ===> Display a suitable question to the user
ans = input('Would you love to sing with me, y or n?: ')
# ===> Accept the user's input (no validation required)

if (ans == 'y'):
    # ===> Add a comment to explain the effect of the last -1 in this call

    for num in range(5, -1, -1):  # theNumber 5 is decreade by one every after one loop
        print(num, "green bottles sitting on the wall")

print("Goodbye")