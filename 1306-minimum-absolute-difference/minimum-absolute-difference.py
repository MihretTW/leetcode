class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr=sorted(arr)
        ans={}
        for i in range(1,len(arr)):
            m=arr[i]-arr[i-1]
            if m in ans:
                ans[m].append([arr[i-1],arr[i]])
            else:
                ans[m]=[[arr[i-1],arr[i]]]
        min_diff=min(ans)
        return ans[min_diff]


