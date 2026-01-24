class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        Transpose_Matrix=[]
        for i in range(len(matrix[0])):
            ans=[]
            for j in range(len(matrix)):
                ans.append(matrix[j][i])
            Transpose_Matrix.append(ans)
        return Transpose_Matrix

        