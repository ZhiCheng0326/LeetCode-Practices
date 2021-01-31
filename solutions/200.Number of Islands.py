class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])

        if nr == 0: return 0

        ans = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    # recursive will stop when no more connecting "1" from current loc (r,c)
                    self.dfs(grid, r, c)
                    ans += 1
        return ans

    def dfs(self, grid, r, c):
        nr = len(grid)
        nc = len(grid[0])

        # mark visited grid to 0 to avoid revisit it
        grid[r][c] = "0"

        for x, y in [(r, c-1),(r, c+1),(r-1, c),(r+1, c)]:
            if 0<=x < nr and 0<=y < nc and grid[x][y]=="1":
                self.dfs(grid, x, y)
