class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if '1' not in s:
            return False
        else:
            conti=True
            n=s.index('1')
            for i in range(n,len(s)):
                if s[i]=='1' and conti==False:
                    return False
                if s[i]=='0':
                    conti=False
            
        return True        