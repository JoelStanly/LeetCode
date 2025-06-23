class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringx = str(x)
        reversex = stringx[::-1]

        if(stringx == reversex):
            return True
        return False