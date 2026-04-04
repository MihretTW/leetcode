class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=Counter(nums)
        return max(m,key=m.get)
       
       