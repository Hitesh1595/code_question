a = 5
b = 3
c = 10

def solve(a, b, c):
    if a > b:
        if a < c:
            return a
        else:
            return max(b,c)
    else:
        if b < c:
            return b
        
        else:
            return max(a,c)

print(solve(5,2,3))