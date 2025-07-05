from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        map1 = Counter(s)
        map2 = Counter(t)

        result = map2 - map1

        
        return list(result.keys())[0]