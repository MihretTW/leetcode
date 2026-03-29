class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        seen=set()
        for i in range(len(ranges)):
            for j in range(ranges[i][0],ranges[i][1]+1):
                seen.add(j)
        print(seen)
        for i in range(left,right+1):
            if i not in seen:
                return False
        return True
        



        