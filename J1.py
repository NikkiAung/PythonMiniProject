# ------------------------------------------------------------
# Import libraries
# ------------------------------------------------------------
# =====> Write your code here


# ------------------------------------------------------------
# Constants
# ------------------------------------------------------------
# =====> Write your code here

# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
myClass = [["Lang", "Carla", 49, 71, 95, 50],
           ["Bucklund", "Pia", 86, 78, 83, 64],
           ["Lang", "Jason", 95, 57, 92, 62],
           ["Dimitrousis", "Hector", 93, 45, 89, 96],
           ["Owens", "Sunna", 45, 50, 46, 54],
           ["Goldin", "Sandra", 25, 60, 45, 55],
           ["Giles", "Seth", 67, 73, 93, 64],
           ["Gurillo", "Melanie", 88, 88, 62, 79],
           ["Rykiel", "Kari", 67, 92, 54, 86],
           ["Shailes", "Dennis", 56, 70, 84, 62]]

# =====> Write your code here
eachTotalMark = []
avg = []
Pass_Fail = []
for index in myClass:
     total_mark = index[2] + index[3] + index[4] + index[5]
     avgMark = total_mark/4
     eachTotalMark.append(total_mark)
     avg.append(avgMark)

for i in range(0,len(avg)):
    if avg[i] > 50:
        Pass_Fail.append('pass')
    elif avg[i] < 50:
        Pass_Fail.append('fail')

    print(myClass[i][0] + myClass[i][1] + ' ' + str(eachTotalMark[i]) + ' ' +str(avg[i]) + ' ' + 'with' + ' ' + Pass_Fail[i])


#print(eachTotalMark)
#print(avg)