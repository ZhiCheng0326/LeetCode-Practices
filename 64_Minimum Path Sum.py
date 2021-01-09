## Method 1: create a table of dp with m rows, n columns
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         dp = [[0]*n for _ in range(m)]

#         for i in range(m):
#             for j in range(n):
#                 if i==0 and j ==0:
#                     dp[i][j] = grid[i][j]
#                 elif i == 0:
#                     # first row can only take in value from prev column
#                     dp[i][j] = grid[i][j]+dp[i][j-1]
#                 elif j == 0:
#                     # first column can only take in value from prev row
#                     dp[i][j] = grid[i][j]+dp[i-1][j]
#                 else:
#                     dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
#         return dp[-1][-1]

## Method 2：use two list to reduce space complexity, prev to record previous row, current to record previous column
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        prev = grid[0][:]
        cur = grid[0][:]

        for i in range(m):
            for j in range(n):
                if i == 0 and j != 0:
                    cur[j] = grid[i][j]+cur[j-1]
                elif i != 0 and j == 0:
                    cur[j] = grid[i][j]+prev[j]
                elif i != 0 and j != 0:
                    cur[j] = grid[i][j]+min(prev[j], cur[j-1])
            prev = cur[:]

        return cur[-1]
