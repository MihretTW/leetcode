class Solution:
    def binaryGap(self, n: int) -> int:
        longest=0
        s=bin(n)
        x=s.index('1')
        for i in range(x+1,len(s)):
            if s[i]=='1':
                y=i-x
                x=i
                longest=max(longest,y)
        return longest
