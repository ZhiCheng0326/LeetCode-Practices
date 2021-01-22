"""
Define region:
[0, p1-1] == 0
[p1, i-1] == 1
[p2+1, n-1] == 2

Therefore, when finish sorting:
[0, p1-1] == 0
[p1, p2] == 1
[p2+1, n-1] == 2
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p1, p2 = 0, n-1
        i = 0

        while i<=p2:
            # print(nums, p1, i, p2)
            if nums[i] == 0:
                nums[i], nums[p1] = nums[p1], nums[i]
                i += 1
                p1 += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
                # because nums[p2] is not visited before, so cannot i+=1
