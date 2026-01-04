class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total=0
        for num in nums:
            sums=0
            count=0
            for i in range(1,int(num**0.5)+1):
                if num%i==0:
                    j=num//i
                    if j==i:
                        sums+=i
                        count+=1
                    else:
                        sums+=i+j
                        count+=2
                if count>4:
                    break
            if count==4:
                total+=sums
        return total