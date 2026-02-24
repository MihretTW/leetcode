class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        right=len(s1)
        count=Counter(s1)
        window_count=Counter()
        for right in range(len(s2)):
            window_count[s2[right]]+=1
            if right-left+1>len(s1):
                window_count[s2[left]]-=1
                if window_count[s2[left]]==0:
                    del window_count[s2[left]]
                left+=1
            if window_count==count:
                return True
        return False
        