class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        s=s.upper()
        for i in range(len(s)):
            ans += (27 - (ord(s[i]) - ord("A") + 1)) * (i + 1)
        return ans
        