class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        l = [row[:] for row in matrix]
        for i in range(n):
            k=0
            for j in range(n-1,-1,-1):
                matrix[i][k]=l[j][i]
                k+=1