class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        count=i=0
        j=1
        while i<j<len(nums):
            if nums[i]<nums[j]:
                count+=1
                i+=1
            j+=1
        
        return count

        