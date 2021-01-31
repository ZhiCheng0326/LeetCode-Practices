class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nr = len(grid)
        nc = len(grid[0])

        ans = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    # recursive will stop when no more connecting "1" from current loc (r,c)
                    area = self.dfs(grid, r, c)
                    ans = max(ans, area)

        return ans

    def dfs(self, grid, r, c):
        nr = len(grid)
        nc = len(grid[0])

        # mark visited grid to 0 to avoid revisit it
        grid[r][c] = 0
        area = 1

        for x, y in [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == 1:
                area += self.dfs(grid, x, y)
                
        return area
