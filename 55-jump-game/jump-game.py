class Solution:
    def canJump(self, nums: List[int]) -> bool:
        prev=nums[0]
        count=0
        for i in range(1,len(nums)):
            if prev==0:
                return False
            if prev>0 and prev<=nums[i]:
                prev=nums[i]
            else:
                prev-=1
            count+=1
        
        return count==len(nums)-1

        