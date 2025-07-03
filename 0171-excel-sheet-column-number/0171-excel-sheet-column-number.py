class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in range(len(columnTitle)):
            result += (ord(columnTitle[i])-ord('A') + 1)* (26 ** (len(columnTitle)-i-1))
        return result