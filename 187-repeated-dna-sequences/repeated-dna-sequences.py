class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i=0
        ans=set()
        for j in range(10,len(s)):
            if s[i:j] in s[i+1:]:
                ans.add(s[i:j])
            i+=1
        return list(ans)
        