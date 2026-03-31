class Solution:
    def finalString(self, s: str) -> str:
        sl=[]
        for i in range(len(s)) :
            if s[i] =='i':
                sl[:i]=sl[:i][::-1]
            else:
                sl.append(s[i])
        return ''.join(sl)
        