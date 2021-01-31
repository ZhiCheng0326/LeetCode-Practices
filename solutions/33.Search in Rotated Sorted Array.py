# Method 1: left region->[left, mid], right region->[mid+1,n-1], therefore mid=(left+right)//2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1

        while left<right:
            mid = (left+right) // 2
            # print(left, mid, right)

            if nums[mid] == target: return mid

            if nums[left] <= nums[mid]:
                # left side is sorted
                if nums[left] <= target <= nums[mid]:
                    # if target is in left side
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # right is sorted
                if nums[mid+1]<= target <= nums[right]:
                    # if target is in right side
                    left = mid + 1
                else:
                    right = mid - 1

        return left if nums[left] == target else -1


# # Method 2: left region->[left, mid-1], right region->[mid,n-1], therefore mid=(left+right+1)//2
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         left = 0
#         right = n-1

#         while left<right:
#             mid = (left+right+1) // 2

#             if nums[mid] == target: return mid

#             if nums[left] < nums[mid]:
#                 # left side is sorted
#                 if nums[left] <= target < nums[mid]:
#                     # if target is in left side
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             else:
#                 # right is sorted
#                 if nums[mid]<= target <= nums[right]:
#                     # if target is in right side
#                     left = mid + 1
#                 else:
#                     right = mid - 1

#         return right if nums[right] == target else -1
