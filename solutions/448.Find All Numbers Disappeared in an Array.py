# Method 1
"""
Time complexity: O(n)
Space complexity: O(1)
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # mark visited elem with -1
        for ind in nums:
            if nums[abs(ind)-1] > 0:
                nums[abs(ind)-1] *= -1

        # index of positive elem = missing numbers in nums
        ans = []
        for i in range(n):
            if nums[i] > 0:
                ans.append(i+1)
        return ans
