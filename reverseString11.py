
x = input('enter a St-Ring: ')
y = x
for k in range(0, len(x)):
    y = y[0:k] + y[-1:] + y[k:-1]


print(y)