# Method 1: DP
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0

        minPrice = prices[0]
        dp = [0]*n

        for i in range(1, n):
            minPrice = min(minPrice, prices[i])
            dp[i] = max(dp[i-1], prices[i] - minPrice)

        return dp[-1]

# # Method 2: Traversal
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         if n == 0: return 0

#         minPrice = prices[0]
#         maxprofit = 0
#         for i in range(n):
#             minPrice = min(minPrice, prices[i])
#             maxprofit = max(maxprofit, prices[i]-minPrice)
#         return maxprofit
