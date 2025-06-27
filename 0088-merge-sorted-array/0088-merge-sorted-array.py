class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:n+m] = sorted(nums1[:m] + nums2[:n])