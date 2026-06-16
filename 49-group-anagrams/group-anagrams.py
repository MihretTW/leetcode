class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for s in strs:
            ss="".join(sorted(s))
            if ss in seen:
                seen[ss].append(s)
            else:
                seen[ss]=[s]
        return list(seen.values())


        