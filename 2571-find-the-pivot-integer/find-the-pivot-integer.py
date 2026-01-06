class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(n,-1,-1):
            x=(i*(i+1))//2
            y=((n-i+1)*(n+i))//2
            if x==y:
                return i
        return -1

        