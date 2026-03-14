class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel={'a', 'e', 'i', 'o', 'u'}
        v={}
        c={}
        for i in range(len(s)):
            if s[i] in vowel:
                if s[i] in v:
                    v[s[i]]+=1
                else:
                    v[s[i]]=1
            else:
                if s[i] in c:
                    c[s[i]]+=1
                else:
                    c[s[i]]=1

        sv=list(v.values())
        sv.sort()
        sc=list(c.values())
        sc.sort()
        max_v = sv[-1] if sv else 0
        max_c = sc[-1] if sc else 0

        return max_v + max_c
        