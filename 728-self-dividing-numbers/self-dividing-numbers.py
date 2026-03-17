class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        for i in range(left,right+1):
            x=list(str(i))
            count=0
            for ch in x:
                if ch=='0':
                    break
                elif i%int(ch)!=0:
                    break
                else:
                    count+=1
            if count==len(x):
                ans.append(i)
        return ans

        