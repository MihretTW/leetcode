class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        l=0
        r=nums.count(1)
        maxs=r
        ans=[0]
        for i in range(len(nums)):
            if nums[i]==0:
                l+=1
            else:
                r-=1
            x=l+r
            if x>maxs:
                maxs=x
                ans=[i+1]
            elif x==maxs:
                ans.append(i+1)
        return ans          