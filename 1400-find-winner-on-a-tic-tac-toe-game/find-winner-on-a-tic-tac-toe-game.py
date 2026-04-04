class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        A,B=[],[]
        for i in range(len(moves)):
            if i%2==0:
                A.append(moves[i])
            else:
                B.append(moves[i])
        dia=[
            [[0,2],[1,1],[2,0]],
            [[0,0],[1,1],[2,2]]
        ]
        for d in dia:
            if all(pos in A for pos in d):
                return "A"
            if all(pos in B for pos in d):
                return 'B'

        
        colA,rowA,colB,rowB=[],[],[],[]

        for i in range(len(A)):
            colA.append(A[i][1])
            rowA.append(A[i][0])

        for r in range(3):
            row=[[r,0],[r,1],[r,2]]
            if all(pos in A for pos in row):
                return "A"
            if all(pos in B for pos in row):
                return 'B'
        for c in range(3):
            col=[[0,c],[1,c],[2,c]]
            if all(pos in A for pos in col):
                return 'A'
            if all(pos in B for pos in col):
                return 'B'
                
        if len(moves)==9:
            return "Draw"
        
        return 'Pending'
        
        

        