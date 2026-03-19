class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        prev = nums[0]
        ans = []
        
        for i in range(len(nums) - 1):
            x = nums[i + 1] - nums[i]
            
            if x != 1:
                if prev == nums[i]:
                    ans.append(str(nums[i]))
                else:
                    ans.append(f"{prev}->{nums[i]}")
                prev = nums[i + 1]
        
        
        if prev == nums[-1]:
            ans.append(str(nums[-1]))
        else:
            ans.append(f"{prev}->{nums[-1]}")
        
        return ans