theString = input('enter a bunch of characters:  ')

theList = []

for x in theString:
    theList.append(x)

tripleList = []
megaList = []
count = 0

for x in range (0, len(theList)):
    if count <= 2:
        tripleList.append(theList[x])
    count = count + 1
    if count == 3:
        megaList.append(tripleList)
        tripleList = []
        count = 0
    if len(theList) - x == 1:
        megaList.append(tripleList)

print(megaList)
