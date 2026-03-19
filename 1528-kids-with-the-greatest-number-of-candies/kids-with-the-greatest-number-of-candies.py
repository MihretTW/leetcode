class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        ans=[]
        for i in range(len(candies)):
            ans.append(m<=candies[i]+extraCandies)
        return ans
        