class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win=Counter(w for w,l in matches)
        loss=Counter(l for w,l in matches)
        ans=[[x for x in win if x not in loss],[x for x in loss if loss[x]==1]]
        ans[1].sort()
        ans[0].sort()
        return ans
        
            


        