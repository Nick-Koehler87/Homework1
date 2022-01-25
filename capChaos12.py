
x = input('Enter a string! ')
alphaList = []

for k in x:
    alphaList.append(k)
lowString = ''
highString= ''
for k in alphaList:
    if k.isupper():
        highString += k
    else:
        lowString += k

print(lowString + highString)