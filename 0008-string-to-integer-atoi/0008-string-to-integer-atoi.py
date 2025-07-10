class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        
        sign = 1
        index = 0
        result = 0
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            sign = 1
            index += 1
        
        while index < len(s) and s[index].isdigit():
            result  = result*10 + int(s[index])
            index += 1
        result *= sign
        
        if result > 2**31 - 1:
            return 2**31 - 1
        if result < -2**31:
            return -2**31
        return result