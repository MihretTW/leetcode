class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans=[]
        m={}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                s=i+j
                if s in m:
                    m[s].append(mat[i][j])
                else:
                    m[s]=[mat[i][j]]
        for key,values in m.items():
            if key%2==0:
                ans.extend(values[::-1])
            else:
                 ans.extend(values)
        return ans