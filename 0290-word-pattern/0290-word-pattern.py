class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        chr_map_s, chr_map_pattern = {},{}
        s = s.split()
        if len(s) != len(pattern):
            return False
        for i in range(len(s)):
            if s[i] not in chr_map_s:
                chr_map_s[s[i]] = i
            if pattern[i] not in chr_map_pattern:
                chr_map_pattern[pattern[i]] = i
            if chr_map_s[s[i]] != chr_map_pattern[pattern[i]]:
                return False
        return True