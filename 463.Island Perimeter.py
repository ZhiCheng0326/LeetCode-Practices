# DFS, slow method, (320ms)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        ans = 0

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    ans = self.dfs(grid, r, c)
                    return ans # return here because only one island

    def dfs(self, grid, r, c):
        nr = len(grid)
        nc = len(grid[0])

        # if fall out of grid, perimeter += 1
        if r < 0 or r >= nr or c < 0 or c >= nc:
            return 1

        # if fall into water, perimeter += 1
        if grid[r][c] == 0:
            return 1

        # if current grid is visited, perimeter += 0
        if grid[r][c] == 2:
            return 0

        # mark visited grid as 2
        grid[r][c] = 2

        perimeter = 0
        for x, y in [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]:
            perimeter += self.dfs(grid, x, y)
        return perimeter
