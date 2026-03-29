class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for ch in strs:
            if str(sorted(ch)) in d:
                d[str(sorted(ch))].append(ch)
            else:
                d[str(sorted(ch))]=[ch]
        return list(d.values())
        