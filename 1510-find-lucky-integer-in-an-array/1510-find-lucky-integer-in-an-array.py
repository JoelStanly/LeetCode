from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash_map = dict(sorted(Counter(arr).items()))
        lucky = -1

        for key,value in hash_map.items():
            if key == value:
                lucky = key
        return lucky