from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_map = Counter(s)
        count = 0
        for i in hash_map.keys():
            count += (hash_map[i]%2)
        if count > 1:
            return len(s) - count + 1
        return len(s)