class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l=0    
        ans=[]
        n=len(p)
        p=sorted(p)
        for r in range(n-1,len(s)):
            x=0
            if sorted(s[l:r+1])==p:  
                ans.append(l)
            l+=1
        return ans
        