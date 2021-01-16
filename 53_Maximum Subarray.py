# Method 1: dp
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        ans = nums[0]

        for i in range(1, n):
            # choose nums[i] or sum it with previous sum
            dp[i] = max(nums[i], nums[i]+dp[i-1])
            # record the max sum achived
            ans = max(dp[i], ans)
        return ans

# # Method 2: space saving dp
# # since dp considers only dp[i-1], use variable to store it, doesn't need to create dp list
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         n = len(nums)
#         ans = prev = nums[0]

#         for i in range(1, n):
#             # choose nums[i] or sum it with previous sum
#             prev = max(nums[i], nums[i]+prev)
#             # record the max sum achived
#             ans = max(prev, ans)
#         return ans
