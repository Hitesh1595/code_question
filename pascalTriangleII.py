# compute pascal row in pascal triangle.......
# complexicity O(k)

def getrow1(self, n):
        res = [1]
        for k in range(1, n + 1):
            res.append(res[-1] * (n + 1 - k) / k)
        return res

def getRow(self, n: int):
        res = []
        def fact(n):
            ans = 1
            for i in range(2,n+1):
                ans *= i
            return ans
        
        for i in range(n + 1):
            res.append(fact(n)//(fact(n-i)*fact(i)))
            
        return res