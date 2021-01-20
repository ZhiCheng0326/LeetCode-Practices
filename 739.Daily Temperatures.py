# Method 1: Stack (484ms, top 99%)
# 1) If T[i] larger than stack[-1], i-stack[-1] to get difference in index, update ans[stack[-1]]
# 2) Repeat step 1 until T[i] smaller than stack[-1], then append T[i] into stack
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(T)

        for ind, val in enumerate(T):

            while stack and val > T[stack[-1]]:
                tmp = stack.pop()
                ans[tmp] = ind - tmp

            stack.append(ind)
        return ans
