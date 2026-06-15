class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s1=Counter(t)
        s2=Counter(s)
        for key, value in s1.items():
            if s2[key] != value:
                return False
        return True

        
        