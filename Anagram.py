a = ['act','dog','god','cat','tac']
def Anagrams(words,n):
    
    d = {}
    
    for i in words:
        sort = "".join(sorted(i))
        
        if sort not in d:
            d[sort] = [i]
        else:
            d[sort].append(i)
    result = []
    
    for i in d:
        result.append(d[i])

    return result
        

ans = Anagrams(a, 5)

for i in ans:
    for word in i:
        print(word, end=' ')
    print()

from collections import Counter
def anagram(str1,str2):
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()

    if len(str1) != len(str2):
        return False
    
    return Counter(str1) == Counter(str2)


str1 = 'public relations'
str2 = 'crap built on lies'


