class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m,n=len(mat),len(mat[0])
        row=[0]*m
        columen=[0]*n

        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    row[i]+=1
                    columen[j]+=1
        return sum(mat[i][j]==1 and row[i]==1 and columen[j]==1
        for i in range(m) for j in range(n))

        

       