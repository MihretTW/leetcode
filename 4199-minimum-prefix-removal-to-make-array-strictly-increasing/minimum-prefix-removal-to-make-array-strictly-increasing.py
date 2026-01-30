class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<=nums[i-1]:
                return i
        return 0
        