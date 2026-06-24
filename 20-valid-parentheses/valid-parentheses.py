class Solution:
    def isValid(self, s: str) -> bool:
        opening=["[", "(", "{"]
        stack=[]
        for ch in s:
            if ch in opening:
                stack.append(ch)
            elif stack==[]:
                return False
            elif ch==")" and stack[-1]=="(":
                stack.pop()
            elif ch=="]" and stack[-1]=="[":
                stack.pop()
            elif ch=="}" and stack[-1]=="{":
                stack.pop()
            else:
                return False
        return stack==[]


