class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for num in nums:
            s=str(num)
            for i in range(len(s)):
                ans.append(int(s[i]))
        return ans