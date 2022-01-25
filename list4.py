

from audioop import add


x = int(input('enter number:'))
y = 0
meggaList = []

for i in range(0, x):
    meggaList.append(float(input('enter annother number:')))

print(meggaList)

for i in meggaList:
    y += i

ave = y/x
print(f'the average is {ave}')
