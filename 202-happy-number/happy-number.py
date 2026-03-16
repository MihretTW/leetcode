class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while True:
            if n==1:
                return True
            if n in seen:
                return False
            seen.add(n)
            x=list(str(n))
            
            for i in range(len(x)):
                x[i]=int(x[i])**2
            n=sum(x)
            
                    

        