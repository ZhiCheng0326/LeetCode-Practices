class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        curColor = image[sr][sc]

        def dfs(r, c):
            # stop dfs if current pixel is modified
            if image[r][c] == newColor: return

            nr = len(image)
            nc = len(image[0])

            image[r][c] = newColor

            for x,y in [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]:
                # only modify pixel same color with image[sr][sc]
                if 0<=x<nr and 0<=y<nc and image[x][y] == curColor:
                    dfs(x, y)

        dfs(sr, sc)
        return image
