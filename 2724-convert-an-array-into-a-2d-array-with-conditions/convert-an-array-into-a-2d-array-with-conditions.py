class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        m=Counter(nums)
        
        d=[[] for _ in range( max(m.values()))]
        print(d)
        for k,v in m.items():
            j=0
            for i in range(v):
                d[j].append(k)
                j+=1

        return d

        