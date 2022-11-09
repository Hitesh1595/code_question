a = [[1]*i for i in range(1,6)]
for i in range(5):
    if i > 1:
        for col in range(1,len(a[i])-1):
            a[i][col] = a[i-1][col-1] + a[i-1][col]

for i in a:
    print(' '*(5-len(i)),end = '')
    print(*i)