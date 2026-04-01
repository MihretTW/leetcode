class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count=0
        for ch in sentences:
            x=1
            for s in ch:
                if s==' ':
                    x+=1
            count=max(count,x)
        return count
        
        