class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer=[]
        for i in range(len(nums)):
            l=sum(nums[:i])
            r=sum(nums[i+1:])
            answer.append(abs(l-r))
        return answer

        