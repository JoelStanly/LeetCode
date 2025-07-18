class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 0
        while(left < len(nums) and right <len(nums)):
            if nums[left] == 0 and nums[right] != 0:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
            elif nums[left] == 0:
                right += 1
            else:
                left += 1
                right = left

        