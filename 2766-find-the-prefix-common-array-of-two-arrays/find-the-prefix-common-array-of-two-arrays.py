class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans=[]
        a=set()
        b=set()
        commen=0
        for i in range(len(A)):
            a.add(A[i])
            b.add(B[i])

            if A[i] in b:
                commen+=1
            if B[i] in a and A[i]!=B[i]:
                commen+=1
            ans.append(commen)
        return ans
            