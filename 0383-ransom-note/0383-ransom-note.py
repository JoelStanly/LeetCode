from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)

        for key,value in ransomNote.items():
            if key not in magazine:
                return False
            if magazine[key] < value:
                return False
        return True