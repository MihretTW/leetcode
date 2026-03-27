class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m=len(matrix),len(matrix[0])
        cols=set()
        rows=set()
        for i in range(n):
            if 0 in matrix[i]:
                rows.add(i)
                for j in range(m):
                    if matrix[i][j]==0:
                        cols.add(j)
        for row in rows:
            for i in range(m):
                matrix[row][i]=0
        for col in cols:
            for i in range(n):
                matrix[i][col]=0
            


                