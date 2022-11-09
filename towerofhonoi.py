# time complexicity O(2^n)
# space O(n)

def Tower_of_honoi(n, a, b, c):
    
    if n >= 1:    
        Tower_of_honoi(n - 1, a, c, b)
        print("move disk {} from {} to {}".format(n,a, c))
        Tower_of_honoi(n - 1, b, a, c)
    
    
        

Tower_of_honoi(3, 'a', 'b', 'c')
