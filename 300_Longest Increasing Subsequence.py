# Method 1: dp (slow, 3528ms)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n

        ans = 1
        for right in range(n):
            # print(dp)
            for left in range(right):
                if nums[left] < nums[right]:
                    dp[right] = max(dp[right], dp[left]+1)
            ans = max(ans, dp[right])

        return ans

# # Method 2: binary search + greedy (fast, 60ms)
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)
#         tails = [nums[0]]

#         for i in range(1, n):

#             if nums[i] > tails[-1]:
#                 # append nums[i] if it is larger than tails[-1]
#                 tails.append(nums[i])
#             else:
#                 # binary search if tails[k] < nums[i], let tails[k+1] = nums[i]
#                 left, right = 0, len(tails)-1
#                 while left<=right:
#                     mid = (left+right) // 2
#                     if tails[mid] >= nums[i]:
#                         loc = mid
#                         right = mid - 1
#                     else:
#                         left = mid + 1
#                 tails[loc] = nums[i]

#         return len(tails)
