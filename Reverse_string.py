def reverse(str1):
    
    return ' '.join(map(str,list(reversed(str1.strip('[]').split(',')))))
    

a = '[1,2,3,4,5,7,8]'

reverse(a)