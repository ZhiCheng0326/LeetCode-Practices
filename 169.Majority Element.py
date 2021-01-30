# # Method 1: sort
"""
Time Complexity: O(nlogn)
Space Complexity: O(logn)
"""
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[len(nums)//2]

# Method 2: hashtable
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hashtable = dict()

        for i in nums:
            if i not in hashtable:
                hashtable[i] = 1
            else:
                hashtable[i] += 1

            if hashtable[i] > n//2:
                return i
