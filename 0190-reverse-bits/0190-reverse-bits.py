class Solution:
    def reverseBits(self, n: int) -> int:
        val = bin(n)[2:].zfill(32)
        reverse = val[::-1]
        return int(reverse,2)