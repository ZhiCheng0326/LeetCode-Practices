class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        isNegative = False if x >= 0 else True
        x = abs(x)

        while x != 0:
            pop = int(x % 10)
            x = x // 10

            if not isNegative and ans > 214748364 or (ans == 214748364 and pop > 7):
                return 0
            if isNegative and ans > 214748364 or (ans == 214748364 and pop > 8):
                return 0

            ans = ans * 10 + pop

        return ans if not isNegative else -1*ans
