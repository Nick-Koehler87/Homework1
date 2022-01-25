print('yo mama fat')

listF = []
listS = []
#whoop
megaList = []


for i in range(0, 5):
    listF.append(int(input('Enter a number!')))
    
for i in range(0, 5):
    listS.append(int(input('Enter a number!')))

for i in listF:
    if i in listS:
        megaList.append(i)

print(megaList)