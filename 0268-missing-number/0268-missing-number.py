from collections import Counter
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mapped = Counter(nums)
        for i in range(len(nums)+1):
            if mapped[i] != 1:
                return i