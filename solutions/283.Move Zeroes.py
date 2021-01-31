# Method 1: Double pointer
"""
Exchange nums[left] and nums[right] if nums[right] != 0
Time complexity: O(n)
Space complexity: O(1)
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        n = len(nums)

        for right in range(n):
            if nums[right] != 0:
                # small optimization, avoid exchanging at same index
                if right > left:
                    nums[left], nums[right] = nums[right], nums[left]
                left += 1
            # print(nums)

# # Method 2: Similar to method 1, replace instead of exchange
# """
# Consider test case: [0,0,0,0,12]
# M2 has to modify nums[i] to 0 from i=1 to i=n-1
# M1 exchange only once, no extra loop required
# Therefore, M1 is more efficient
# """
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         left = 0
#         n = len(nums)

#         for right in range(n):
#             if nums[right] != 0:
#                 nums[left] = nums[right]
#                 left += 1

#         for i in range(left, n):
#             nums[i] = 0
