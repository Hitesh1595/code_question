# omly two duplictes value is allowed 

def removeDuplicates(lst):
        s = e = 0

        while e < len(lst):
            if lst[s] == lst[e]:
                if e-s > 1:
                    lst.pop(s)

                else:
                    e += 1
            else:
                s = e

        print(lst)
lst = [1,2,2,2,3,3,3,6,6,6]
removeDuplicates(lst)