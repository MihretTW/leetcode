class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        print(strs)
        ans=''
        
        for i in range(len(strs[0])):
            count=0
            for j in range(1,len(strs)):
                if strs[0][i]==strs[j][i]:
                    count+=1
                else:
                    return ans
            if count==len(strs)-1:
                ans+=strs[0][i]
        return ans
