# Method 1: Sort + side by side compare
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False

# # Method 2: if len(set(nums)) != len(nums), return False
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         if len(set(nums))!=len(nums):
#             return True
#         return False

# # Method 3: Hashtable
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         Hashtable = set()
#         for i in nums:
#             if i in Hashtable:
#                 return True
#             Hashtable.add(i)
#         return False
