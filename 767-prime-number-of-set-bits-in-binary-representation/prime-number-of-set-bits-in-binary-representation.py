class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime=[ 2, 3, 5, 7, 11, 13, 17,19]
        count=0
        for i in range(left,right+1):
            x=str(bin(i))
            y=x.count('1')
            if y in prime:
                count+=1
        return count
        