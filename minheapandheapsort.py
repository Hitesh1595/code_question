
def minheapify(arr,n, i):
    p = i
    l = 2 * i +1
    r = 2 * i + 2

    if l < n and arr[l] < arr[i]:
        p = l
    if r < n and arr[r] < arr[p]:
        p = r
    
    if p != i:
        arr[p], arr[i] = arr[i], arr[p]
        minheapify(arr, n, p)
        
    

    
def heap(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        minheapify(arr, len(arr), i)
        
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        minheapify(arr,i,0)
        
    


arr = [4, 10, 3, 5, 1]
heap(arr)
print(arr)