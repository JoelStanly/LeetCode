class Solution:
    def possibleStringCount(self, word: str) -> int:
        prev = ""
        output = 1
        for i in range(len(word)):
            if prev == word[i]:
                output += 1
            prev = word[i]
        return output