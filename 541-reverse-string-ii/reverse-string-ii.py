class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        sl=list(s)
        
        for i in range(0,len(s),2*k):
            sl[i:i+k]= sl[i:i+k][::-1]
        
        return "".join(sl)
        