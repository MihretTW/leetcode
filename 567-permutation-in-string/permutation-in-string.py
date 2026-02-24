class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        right=len(s1)
        s1=sorted(s1)
        while left<right<=len(s2):
            if sorted(s2[left:right])==s1:
                return True
            else:
                left+=1
                right+=1
        return False
        