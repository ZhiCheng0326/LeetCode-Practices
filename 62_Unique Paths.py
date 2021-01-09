# Method 1: create a table of dp with m rows, n columns
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

# # # Method 2：use two list to reduce space complexity, prev to record previous row, current to record previous column
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:

#         prev = [1]*n
#         cur = [1]*n
#         for i in range(1,m):
#             for j in range(1,n):
#                 cur [j] = cur[j-1] + prev[j]
#             prev = cur[:]
#         return cur[-1]
