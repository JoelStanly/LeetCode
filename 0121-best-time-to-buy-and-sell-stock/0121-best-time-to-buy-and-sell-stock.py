class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highProfit = 0
        lowProfit = prices[0]
        for i in prices[1:]:
            if i < lowProfit:
                lowProfit = i
            highProfit = max(highProfit,i - lowProfit)
        return highProfit