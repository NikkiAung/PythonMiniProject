# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
sweetTable = [["Choco Drops", 13, 8.12],
              ["Aniseed Pyramids", 18, 2.11],
              ["Ice Cream Swirls", 12, 6.21],
              ["Caramel Bobs", 16, 4.94],
              ["Fluffy Clouds", 14, 5.61],
              ["Tangy Teeth", 13, 1.96],
              ["Minty", 14, 1.77],
              ["Cobblers", 14, 6.62],
              ["Chomps", 12, 4.63],
              ["Fruit Fizz", 14, 7.04]]

outLine = ""
total = 0.0

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
# Open the file for write only
file = open ("ngl.txt", "w")

# Access each record in the table one at a time
for sweet in sweetTable:
    # Pick up each field, convert data types if required
    outLine = sweet[0] + ","
    outLine = outLine + str (sweet[1])
    outLine = outLine + ","
    outLine = outLine + str (sweet[2])
    outLine = outLine + ","

    # Calculate total price of inventory in stock
    total = sweet[1] * sweet[2]
    total = round (total, 2)    # Round to currency
    outLine = outLine + str (total)

    # Add the line feed
    outLine = outLine + "\n"

    # Write the line to the file
    file.write (outLine)

file.close ()
