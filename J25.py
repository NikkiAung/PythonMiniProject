# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------

classTable = []


# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def showClass():
    if (len(classTable) != 0):
        for student in classTable:
            print(student)
    else:
        print("----- Table is empty -----")


def loadData(pID, pLast, pFirst, pBirth, pBalance):
    aRecord = []
    aRecord.append(pID)
    aRecord.append(pLast)
    aRecord.append(pFirst)
    aRecord.append(pBirth)
    aRecord.append(pBalance)

    # Append it to the class table
    classTable.append(aRecord)
    #showClass()
print("\n... Appending three records ...")
loadData(384, "Collins", "Ivy", 2010, 15.34)
loadData(405, "Brown", "James", 2011, 18.87)
loadData(410, "Jones", "Karen", 2010, 12.98)
showClass()

def inserting(newRecord):
    classTable.insert(1,newRecord)
    showClass()


print('\n inserting a new record at position [1]')
newRecord = [813, 'Lee', 'Charles', 2009, 5.47]
inserting(newRecord)

print('\n Deleting record at position [2] ... ')
for item in classTable:
    if item == classTable[2]:
        classTable.remove(item)

for x in classTable:
    print(x)


