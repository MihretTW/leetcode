class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=0
        y=0
        for num in gain:
            y+=num
            n=max(n,y)
    
        return n

        