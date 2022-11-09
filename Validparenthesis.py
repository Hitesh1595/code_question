# time O(n)
# space O(n)
def ispar(x):
    s = '[{('
    e = '}])'
    
    stack = []
    
    if len(x) %2 == 1:
        return False
        
 
    for i in x:
        if i in s:
            stack.append(i)
        else:
            if len(stack) != 0  and stack[-1] == '[':
                stack.pop()
            elif len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            elif len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            else:
                return False
                 
    if len(stack) == 0:
        return True
    else:
        return False
        

print(ispar('{([])}'))