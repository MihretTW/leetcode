class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans=0
        odd=False
        m=Counter(s)
        for freq in m.values():
            ans+=freq//2 *2
            if freq%2==1:
                odd=True
        if odd:
            ans+=1
        return ans