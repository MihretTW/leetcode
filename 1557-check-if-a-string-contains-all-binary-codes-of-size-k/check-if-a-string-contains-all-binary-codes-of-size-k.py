class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen=set()
        l=0
        for r in range(k,len(s)+1):
            seen.add(s[l:r])
            l+=1
        return len(seen)==2**k

                
        