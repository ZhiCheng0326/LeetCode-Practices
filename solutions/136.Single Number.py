# Because questions require O(n) complextiy and O(1) memory
# therefore, use bit operation
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]
        return ans
