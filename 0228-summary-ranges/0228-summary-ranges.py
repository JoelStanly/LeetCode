class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        returnValue = ''
        result = []
        i = 0
        while i<len(nums):
            if returnValue=='':
                returnValue += str(nums[i])
                prev = nums[i]
                idx = i
                i += 1
            elif nums[i] == prev + 1:
                prev = nums[i]
                i += 1
            elif i-1 == idx:
                result.append(returnValue)
                returnValue = ''
            else:
                result.append(returnValue+"->"+str(nums[i-1]))
                returnValue = ''

        if returnValue != '':
            if i-1 == idx:
                result.append(returnValue)
            else:
                result.append(returnValue+"->"+str(nums[i-1]))
        return result