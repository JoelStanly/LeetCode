class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber > 0:
            columnNumber -= 1
            remaining = columnNumber % 26
            result += chr(ord("A")+ remaining)
            columnNumber //= 26
        return result[::-1]