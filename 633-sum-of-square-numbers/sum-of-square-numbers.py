class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        j=int(sqrt(c))
        i=0
        while i<=j:
            n=i*i + j*j
            if n==c:
                return True
            elif n>c:
                j-=1
            else:
                i+=1
        return False
        