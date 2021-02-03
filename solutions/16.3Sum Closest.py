# Method: Double pointer
"""
'i' loop through each element in nums, with nums[i], change 'left', 'right' pointer to find closest sum
Time complexity: O(n)
Space complexity: O(n)
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        min_dist = math.inf
        ans = None
        for i in range(n):
            # pruning, array is sorted, with same nums[i] will get same ans
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # update 'ans' and 'min_dist'
                if abs(target-total) < min_dist:
                    ans = total
                    min_dist = abs(target-total)

                # make decision to move left or right pointer
                if total < target:
                   left += 1

                elif total > target:
                    right -= 1

                else :
                    ans = total
                    return ans
        return ans
