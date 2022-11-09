def solve(lst):
    s = 0
    h = len(lst)-1
    m = 0

    while m <= h:
        if lst[m] == 0:
            lst[m],lst[s] = lst[s],lst[m]
            s += 1
            m += 1
        elif lst[m] == 1:
            m += 1
        else:
            lst[m],lst[h] = lst[h],lst[m]
            h -= 1

    print(lst)





lst = [1,1,0]

solve(lst)