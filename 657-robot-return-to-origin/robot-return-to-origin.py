class Solution:
    def judgeCircle(self, moves: str) -> bool:
        RL=0
        UD=0
        for ch in moves:
            if ch=='U' :
                UD+=1
            elif ch=='R':
                RL+=1
            elif  ch=='L' :
                RL-=1  
            else:
                UD-=1
        return RL==0 and UD==0
        