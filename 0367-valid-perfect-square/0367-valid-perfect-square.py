class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(num+1):
            if i ** 2 > num:
                return False
            elif i ** 2 == num:
                return True
        return False