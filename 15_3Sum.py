"""
Sort then use double pointer pointing head and tail

Steps to avoid duplicate:
* if nums[i] ==  nums[i-1]: i+=1
* if nums[left] == nums[left+1]: left+=1
* if nums[right] == nums[right-1]: right+=1

Early stopping:
if nums[i] > 0: break
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n <3: return []
        nums.sort()

        ans = []
        for i in range(n):
            left = i+1
            right = n-1
            if nums[i] > 0: break

            while(left<right):
                if i > 0 and nums[i] == nums[i-1]: break

                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -=1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left +=1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1
                    left +=1 # can comment out either left or right
                    right -=1
        return ans
