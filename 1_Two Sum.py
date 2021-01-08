## brute force method
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)

#         for i in range(n):
#             new_nums = nums[i+1:]
#             ptr = i+1
#             if target-nums[i] in new_nums:
#                 while ptr < n and nums[ptr] != target-nums[i]: ptr +=1

#                 return [i, ptr]


## hash table method
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashtable = dict()

        # find target-nums[i] from hashtable
        for j in range(n):
            if target-nums[j] in hashtable:
                return [j, hashtable[target-nums[j]]]
            # build hashtable
            hashtable[nums[j]] = j
