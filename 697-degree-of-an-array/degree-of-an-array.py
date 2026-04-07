from collections import Counter
from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        m = Counter(nums)
        max_freq = max(m.values())
        min_len = len(nums)
        
        for num, freq in m.items():
            if freq == max_freq:
                first_idx = nums.index(num)
                last_idx = len(nums) - 1 - nums[::-1].index(num)
                min_len = min(min_len, last_idx - first_idx + 1)
        
        return min_len