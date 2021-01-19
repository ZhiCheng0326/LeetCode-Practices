# # Method 1: Dp, Bottom-up method (1324ms)
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [float('inf')] * (amount+1)
#         dp[0] = 0

#         for target in range(1, amount+1):
#             for c in coins:
#                 if target-c >= 0:
#                     dp[target] = min(dp[target], dp[target-c]+1)

#         if dp[-1] == float('inf'):
#             return -1
#         else:
#             return dp[-1]


# Method 2: Dfs + pruning (160ms)
"""
Test case
Input:
[1,7,10]
14
Output:
2

Pruning:
    If k + count > self.ans, stop the loop, because continuing the loop will only take in more coins. (because loop continue to take coins of lesser value)

Note that k in descending order
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        self.ans = float('inf')

        def dfs(coins, amount, c_index, count):
            if amount == 0:
                self.ans = min(self.ans, count)
                return

            if c_index == len(coins):
                return

            for k in range(amount//coins[c_index],-1,-1):
                if k + count < self.ans:
                    dfs(coins, amount - k * coins[c_index], c_index + 1, count + k)
                else:
                    # pruning (important!!!)
                    break
        dfs(coins, amount, 0, 0)

        return self.ans if self.ans != float('inf') else -1
