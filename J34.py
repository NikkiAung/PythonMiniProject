# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
sweetTable = []
fields = []
total = 0.0

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
# Open file read only
file = open ("sweet.txt", "r")

# Read each line one at a time
for line in file:
    # Remove the line feed
    line = line.strip ()

    # Separate the fields
    fields = line.split (",")

    # Make a new record and convert data types
    sweet = []
    sweet.append (fields[0])
    sweet.append (int (fields[1]))
    sweet.append (float (fields[2]))

    # Calculate additional inventory column and add to record
    total = sweet[1] * sweet[2]
    total = round (total, 2)
    sweet.append (total)

    # Add the new record
    sweetTable.append (sweet)

file.close ()       # Close when finished

# Display for verification
print (sweetTable[0])
print (sweetTable[len (sweetTable) - 1])