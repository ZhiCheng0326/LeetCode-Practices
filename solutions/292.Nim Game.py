# n = 4, 8, 12, 16... will make you lose the game
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
