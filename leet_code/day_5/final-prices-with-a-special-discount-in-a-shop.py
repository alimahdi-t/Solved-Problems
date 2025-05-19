class Solution:
    def finalPrices(self, prices):
        arr = []
        for i in range(len(prices)):
            x = prices[i]
            for j in range(i + 1, len(prices) - 1):
                if prices[j] <= prices[i] and j > i:
                    x = prices[i] - prices[j]
                    break
            prices[i] = x
        return prices


s = Solution()
print(s.finalPrices([8,4,6,2,3]))
