class Solution:
    def mySqrt(self, x: int) -> int:
        output = 1
        while output * output <= x:
            output += 1
        return output - 1