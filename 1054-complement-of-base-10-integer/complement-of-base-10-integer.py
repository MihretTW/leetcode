class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x=bin(n)[2:]
        s=''
        for i in range(len(x)):
            if x[i]=='0':
                s+='1'
            else:
                s+='0'
        return int(s,2)
                
        