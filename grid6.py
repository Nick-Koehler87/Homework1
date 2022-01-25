
row = int(input('enter a row number fron 1 to 5 Boyyyy:'))
col = int(input('eneter a coulum number fron 1 to 5 gurlll:'))

for i in range(1, 6):
    for k in range(1, 6):
        if row == i and col == k:
            print('1 ', end='')
        else:
            print('0 ', end='')   
        if k == 5:
            print('')
        