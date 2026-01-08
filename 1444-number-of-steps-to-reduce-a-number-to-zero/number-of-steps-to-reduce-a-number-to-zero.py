class Solution:
    def numberOfSteps(self, n: int) -> int:
        count=0
        while n>0:
            if n%2==0:
                count+=1
                n=n//2
            else:
                count+=1
                n-=1
        
        return count
        