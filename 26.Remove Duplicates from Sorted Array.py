class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0

        for right in range(1,n):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]

        return left+1
