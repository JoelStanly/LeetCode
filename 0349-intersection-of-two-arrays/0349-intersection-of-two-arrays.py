class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(set(nums1))
        nums2 = sorted(set(nums2))
        result = []
        for value in nums1:
            if value in nums2:
                result.append(value)
        return result