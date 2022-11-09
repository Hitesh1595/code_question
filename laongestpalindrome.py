# to i index check left and right and update and return the value
def longestpalindrome(str1):
    n = len(str1)
    if n <= 1:
        return str1

    Max = 1
    st, ed = 0, 0

    if n % 2 == 0:
        for i in range(1, n - 1):
            l, r = i, i + 1
            while l >= 0 and r <= n - 1:
                if str1[l] == str1[r]:
                    l -= 1
                    r += 1
                else:
                    break
            len1 = r-l-1
            if len1 > Max:
                Max = len1
                st = l+1
                ed = r - 1
                
            
    else:
        for i in range(1, n - 1):
            l, r = i, i 
            while l >= 0 and r <= n - 1:
                if str1[l] == str1[r]:
                    l -= 1
                    r += 1
                else:
                    break
            len1 = r-l - 1
            if len1 > Max:
                Max = len1
                st = l+1
                ed = r - 1

    return str1[st:ed+1]
    
    
ans = longestpalindrome('abbbb')
print(ans)