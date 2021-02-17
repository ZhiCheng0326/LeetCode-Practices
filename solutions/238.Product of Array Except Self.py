# """
# Method 1: Use 'left', 'right' array to store multiplication from left and right

# Time complexity: O(n)
# Space complexity: O(n)
# """
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         ans = [1] * n

#         left = [1] * n
#         right = [1] * n

#         for i in range(n-1):
#             left[i+1] = nums[i]*left[i]

#         for i in range(n-1, 0, -1):
#             right[i-1] = nums[i]*right[i]

#         print(left)
#         print(right)

#         ans = []
#         for i in range(n):
#             ans.append(left[i]*right[i])

#         return ans

# """
# Method 2: Use output array to store multiplication from left, then multiply again from right

# Time complexity: O(n)
# Space complexity: O(1) # ignoring space took up by output array
# """
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         ans = [1] * n

#         # ans[i] = ans[0]*...*ans[i-1]
#         for i in range(1, n):
#             ans[i] = ans[i-1] * nums[i-1]

#         # ans[i] = (ans[0]*...*ans[i-1]) * (ans[i+1]*...*ans[n-1])
#         right = 1
#         for i in range(n-1, -1, -1):
#             ans[i] = ans[i] * right
#             right *= nums[i]

#         return ans

"""
Method 3: Single traversal
Time complexity: O(n)
Space complexity: O(1) # ignoring space took up by output array
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        left = right = 1
        for i in range(n):
            ans[i] *= left
            left *= nums[i]

            ans[n-1-i] *= right
            right *= nums[n-1-i]

            # print(ans, left, right)

        return ans
