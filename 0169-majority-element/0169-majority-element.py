from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hashtable = Counter(nums)

        for k,v in hashtable.items():
            if v > n/2:
                return k