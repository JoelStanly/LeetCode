class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        left = m-1
        right = n+m-1
        comp = n-1

        while comp>=0 and left>=0 and right>=0:
            if nums2[comp] >= nums1[left]:
                nums1[right] = nums2[comp]
                right -= 1
                comp -= 1
            else:
                nums1[right] = nums1[left]
                left -= 1
                right -= 1
            print(left,right,nums1)
        while comp>=0 and right>=0:
            print(right,comp,nums2[comp])
            nums1[right] = nums2[comp]
            right -= 1
            comp -= 1
        return nums1