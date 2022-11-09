#timecomplexicity  O(row*col)
# space O(1)
def spirallyTraverse(matrix, r, c): 
    
    firstrow  = 0
    lastrow = r
    firstcol = 0
    lastcol = c
    while firstrow < lastrow and firstcol < lastcol:
        # firstrow
        for i in range(firstcol,lastcol):
            print(matrix[firstrow][i],end = ' ')
        firstrow += 1
        # lastcol
        for i in range(firstrow,lastrow):
            print(matrix[i][lastcol-1],end = ' ')
        lastcol -= 1
        if firstrow < lastrow:
        # last row
            for i in range(lastcol-1,firstcol-1,-1):
                print(matrix[lastrow-1][i],end = ' ')
            lastrow -= 1
        if firstcol < lastcol:
        # first col
            for i in range(lastrow-1,firstrow-1,-1):
                print(matrix[i][firstcol],end = ' ')
            firstcol += 1
r = 3
c = 6
arr = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]
spirallyTraverse(arr, r, c)
# 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11 


