class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        seen=set()
        for i in range(len(ranges)):
            seen.update(x for x in range(ranges[i][0],ranges[i][1]+1))
        print(seen)
        for i in range(left,right+1):
            if i not in seen:
                return False
        return True
        



        