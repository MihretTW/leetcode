class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        count1=0
        count2=0
        
        for i in range(0,n,2):
            if s[i]!='0':
                count1+=1
        for i in range(1,n,2):
            if s[i]!='1':
                count1+=1
    
        for i in range(0,n,2):
            if s[i]!='1':
                count2+=1
        for i in range(1,n,2):
            if s[i]!='0':
                count2+=1

        return min(count1,count2)
        