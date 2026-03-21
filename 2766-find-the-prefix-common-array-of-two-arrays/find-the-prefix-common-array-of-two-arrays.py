class Solution:
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        res = []

        for i in range(n):
            count = 0
            
            for j in range(i + 1):  
                for k in range(i + 1):  
                    if A[j] == B[k]:
                        count += 1
                        break   
            
            res.append(count)

        return res