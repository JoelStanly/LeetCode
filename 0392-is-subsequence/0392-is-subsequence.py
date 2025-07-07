class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        while(j < len(t)):
            if i == len(s):
                return True
            if t[j] == s[i]:
                i += 1
            j += 1
        if i == len(s):
            return True
        return False