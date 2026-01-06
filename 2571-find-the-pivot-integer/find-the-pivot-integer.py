class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(n,-1,-1):
            x=sum(range(1,i+1))
            y=sum(range(i,n+1))
            if x==y:
                return i
        return -1

        