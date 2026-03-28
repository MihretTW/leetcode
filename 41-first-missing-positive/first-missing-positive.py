class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums = sorted(set(nums))
        expected = 1  
        
        for num in nums:
            if num < 1:
                continue
            if num == expected:
                expected += 1
            elif num > expected:
                
                return expected
        
        return expected