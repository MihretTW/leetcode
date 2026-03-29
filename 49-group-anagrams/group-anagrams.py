class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for ch in strs: 
            d[str(sorted(ch))].append(ch)      
        return list(d.values())
        