class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1,-1]
        first_pos = self.find_first_last_position(nums, target, True, 0)

        if first_pos == -1:
            return [-1, -1]

        last_pos = self.find_first_last_position(nums, target, False, first_pos)

        return [first_pos, last_pos]

    def find_first_last_position(self, nums, target, find_first, left):
        n = len(nums)
        right = n-1
        while left < right:
            # (left+right+1)//2 to avoid infinite loop
            mid = (left + right) // 2 if find_first else (left+right+1)//2
            if target < nums[mid]:
                right = mid-1
            elif target > nums[mid]:
                left = mid + 1
            else:
                if find_first:
                    # look for target in left side
                    right = mid
                else:
                    # look for target in right side
                    left = mid

        # check if target in nums
        if nums[left] == target:
            return left
        else:
            return -1
