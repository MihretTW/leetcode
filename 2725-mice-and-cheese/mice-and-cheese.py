class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diff=[]
        for i in range(len(reward1)):
            diff.append(reward1[i]-reward2[i])
        diff.sort(reverse=True)
        return sum(reward2)+sum(diff[:k])
        