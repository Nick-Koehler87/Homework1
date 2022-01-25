cont = True
megaList = []
while cont:
    x = input('enter a number or "Quit" to Quit:')
    if x == 'Quit':
        cont = False
    else:
        megaList.append(int(x))

print(megaList)