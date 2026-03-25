class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        x=nums[0]
        count=1
        if len(nums)==1:
            return nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                count+=1
            else:
                x=nums[i]
                count=1
            if count>len(nums)//2:
                return nums[i]
        