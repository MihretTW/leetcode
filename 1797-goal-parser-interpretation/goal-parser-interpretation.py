class Solution:
    def interpret(self, command: str) -> str:
        ans=''
        temp=''
        for ch in command:
            if ch=="G":
                ans+=ch
            else:
                temp+=ch
                if temp=='()':
                    ans+='o'
                    temp=''
                elif temp=='(al)':
                    ans+="al"
                    temp=''
        return ans
                

        