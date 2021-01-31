class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x^y
        ans = 0
        while res:
            if res&1:
                ans += 1
            res = res >> 1

        return ans
