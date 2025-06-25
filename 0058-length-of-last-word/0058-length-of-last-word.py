class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        values = s.split()
        return len(values[-1])