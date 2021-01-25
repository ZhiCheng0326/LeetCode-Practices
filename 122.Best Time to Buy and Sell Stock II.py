# # Method 1: greedy method (36ms)
# # Sell stock if prices[i] is larger than prices[i-1]
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         ans = 0
#         n = len(prices)
#         for i in range(1, n):
#             if prices[i] > prices[i-1]:
#                 ans += prices[i] - prices[i-1]
#         return ans

# Method 2: dp
"""
dp array stores the accumulated profit
if decision = buy, dp - prices[i], elif decision = sell, dp + prices[i]
dp[i][0] means after transaction on day i-th, not holding stock
dp[i][1] means after transaction on day i-th, holding 1 stock
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0,0] for _ in range(n)]

        # Initialization
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        # dp here
        for i in range(1,n):
            # print(dp)
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[-1][0]
