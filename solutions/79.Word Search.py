class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nr = len(board)
        nc = len(board[0])
        n = len(word)

        # mark visited board[r][c] as False
        marked = [[True for _ in range(nc)] for _ in range(nr)]

        target = 0
        for r in range(nr):
            for c in range(nc):
                if board[r][c] == word[target]:
                    found = self.dfs(board, r, c, word, marked, target)
                    if found:
                        return True
        return False

    def dfs(self, board, r, c, word, marked, target):
        nr = len(board)
        nc = len(board[0])
        n = len(word)

        if target == n-1:
            return board[r][c]==word[target]

        # mark visited grid as False
        marked[r][c] = False

        for x, y in [(r, c-1),(r, c+1),(r-1, c),(r+1, c)]:
            if 0<=x < nr and 0<=y < nc and marked[x][y] and board[x][y]==word[target+1]:
                found = self.dfs(board, x, y, word, marked, target+1)

                if found:
                    return True

        # release visited grid and mark as True
        marked[r][c] = True

        return False
