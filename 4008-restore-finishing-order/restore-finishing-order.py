class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        f = set(friends)
        return [x for x in order if x in f]
