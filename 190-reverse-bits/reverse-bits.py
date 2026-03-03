class Solution:
    def reverseBits(self, n: int) -> int:
        x=bin(n)[2:]
        x=x.zfill(32)
        return int(x[::-1],2)
        