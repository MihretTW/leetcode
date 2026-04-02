class Solution:
    def countCollisions(self, directions: str) -> int:
        stack=[]
        collision=0
        for ch in directions:
            while stack and ( (stack[-1]=='R' and ch in 'SL') or (stack[-1]=='S' and ch=='L') ):
                if stack[-1]=="S" and ch=='L':
                    collision+=1
                    ch='S'
                elif stack[-1]=='R' and ch=='S':
                    collision+=1
                    stack.pop()
                    ch='S'
                   
                elif stack[-1]=='R' and ch=='L':
                    collision+=2
                    stack.pop()
                    ch='S'
                    
                else:
                    break
            
            stack.append(ch)
        return collision
        