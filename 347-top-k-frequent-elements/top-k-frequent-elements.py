class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m=Counter(nums)
        sm=sorted(m.items(), key=lambda x:x[1], reverse=True)
        return [num for num, freq in sm[:k]]