class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        arr=[]
        for i in range(len(bank)):
            x=bank[i].count('1')
            if x!=0:
                arr.append(x)
        if len(arr)==0:
            return 0
        else:
            ans=0
            for i in range(len(arr)-1):
                ans+=arr[i]*arr[i+1]
            return ans

        