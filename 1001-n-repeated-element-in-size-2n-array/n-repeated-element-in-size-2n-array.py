class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        m=Counter(nums)
        for v in m:
            if m[v]>1:
                return v



        