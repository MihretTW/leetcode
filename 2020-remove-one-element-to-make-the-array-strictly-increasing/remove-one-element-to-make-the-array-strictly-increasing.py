class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            n = nums[:i] + nums[i+1:]
            m = sorted(n)  # returns a new sorted list
            if n == m and len(set(n)) == len(n):  # strictly increasing
                return True
        return False