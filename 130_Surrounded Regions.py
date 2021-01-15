"""
1) Start dfs from boundaries with letter "O"
2) Mark all "O" connecting with boundaries to "#", as it is not surrounded by "X"
3) dfs completed
4) loop through each grid, change "O" to "X" and "#" to "O"
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0: return []
        nr = len(board)
        nc = len(board[0])

        # begin dfs from boundaries with letter "O"
        for r in range(nr):
            for c in range(nc):
                if r == 0 or r == nr-1 or c == 0 or c == nc-1:
                    if board[r][c] == "O":
                        self.dfs(board, r, c)

        # change "O" to "X" and "#" to "O"
        for r in range(nr):
            for c in range(nc):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"

    def dfs(self, board, r, c):
        nr = len(board)
        nc = len(board[0])

        board[r][c] = "#"
        for x, y in [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]:
            if 0<=x<nr and 0<=y<nc and board[x][y] == "O":
                self.dfs(board, x, y)
