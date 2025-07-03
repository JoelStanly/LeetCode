class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex += 1
        dp = [[0]*(i+1) for i in range(rowIndex)]

        for i in range(rowIndex):
            dp[i][0] = 1
            dp[i][i] = 1

            for j in range(1,i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp[rowIndex-1]