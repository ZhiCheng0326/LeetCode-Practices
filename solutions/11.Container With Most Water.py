# Method 1: Double pointer
"""
Always move the pointer pointing at lower height.
This is because if move pointer at higher height, area will not change
area = distance * min(height[left], height[right])

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        n = len(height)
        left, right = 0, n-1

        while left< right:
            distance = right - left
            area = max(area, distance * min(height[left], height[right]))

            # move the pointer pointing at lower height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
