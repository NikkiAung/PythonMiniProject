# -------------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------------
# ===> Import a library to use Pi
import math

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------

# Hard coded for testing
coneHeight = 10.7
baseRadius = 1.2
coneVolume = 0.0

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# ===> Add parameters inside the brackets
def calcVolume (pHeight,pRadius):

    print ("The radius is:", pRadius)
    print ("The height is:", pHeight)

    # ===> Complete the calculation for the volume
    theVolume = 1/3 * math.pi * pRadius * pHeight

    print ("The volume is:", theVolume)

    return theVolume

    # ===> Return the volume to the caller


# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
coneVolume = calcVolume (coneHeight,baseRadius)

# ===> Call the subprogram, passing parameters,
#      and catch the returned value in the correct variable


# ===> Print the total volume to three decimal places using string.format()
# ===> by completing the pattern inside the { }
print("{:.3f}".format(coneVolume))











