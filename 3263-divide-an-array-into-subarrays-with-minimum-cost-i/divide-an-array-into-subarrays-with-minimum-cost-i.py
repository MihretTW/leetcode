class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        x=nums[0]
        nums.remove(nums[0])
        nums.sort()
        return x+nums[0]+nums[1]

        