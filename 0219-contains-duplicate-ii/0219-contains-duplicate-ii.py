class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexMap = {}
        for i,num in enumerate(nums):
            if num in indexMap and abs(i - indexMap[num]) <=k:
                return True
            indexMap[num] = i
        return False