class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans=0
        for i in range(len(t)):
            x=s.index(t[i])
            ans+=abs(i-x)
        return ans
        