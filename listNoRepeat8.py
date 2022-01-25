megaList = []
notList = []
print('Enter 10 numbers')

for x in range(1, 11):
    lmao = input(f'{x} input: ')
    if not lmao in megaList:
        megaList.append(lmao)
    else:
        notList.append(lmao)

for x in megaList: 
    if x in notList:
        megaList.remove(x)

print(megaList)