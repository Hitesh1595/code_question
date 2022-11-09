# time O(log(row)+log(col))
# space O(1)
def searchmatrix(matrix, target):
    if not matrix:
        return False
    if not matrix[0]:
        return False
    r = -1
    r1, r2 = 0, len(matrix) - 1
    while r1 <= r2:
        row = r1 + (r2-r1)//2
        if matrix[row][0] <= target <= matrix[row][-1]:
            r = row
            break
        elif matrix[row][0] > target:
            r2 = row - 1
        else:
            r1 = row + 1
            
    if r == -1:
        return False
    
    c1 = 0
    c2 = len(matrix[0])
    while c1 <= c2:
        mid = c1 + (c2 - c1) // 2
        if matrix[r][mid] == target:
            return True
        elif matrix[r][mid] > target:
            c2 = mid - 1
        else:
            c1 = mid + 1
            
    
    


matrix = [[]]
target = 100
ans = searchmatrix(matrix, target)
print(ans)