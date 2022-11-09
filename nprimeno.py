# time complexicity O(sqrt(n)log(log(n)))

n = int(input())
arr = [True]*(n+1)

j = 2

while j*j <= n:
    
    if arr[j]:
        for i in range(j*j,n+1,j):
            arr[i] = False
            
    
    j += 1

for i in range(2,n+1):
    if arr[i]:
        print(i,end = ' ')