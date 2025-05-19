class Solution:
    def generate(self, numRows: int):
        if numRows == 1:
            return [[1]]
        dp = [[1 if j + 1 == i or j == 0 else 0 for j in range(i)] for i in range(1, numRows + 1)]
        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp



s = Solution()
print(s.generate(5))