from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_s = Counter(s)
        map_t = Counter(t)

        for i in map_s:
            if map_t[i] != map_s[i]:
                return False
        return True
        