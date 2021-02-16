"""
Time complexity: O(n^2)
Space complexity: O(n^2)
"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # init matrix
        mat = [[0]*n for _ in range(n)]

        # define boundaries
        top, bottom = 0, n-1
        left, right = 0, n-1

        # define current value, i and target
        i = 1
        target = n**2

        # x loop through rows, y loop through columns
        while i <= target:
            # left to right
            x = top
            for y in range(left, right+1):
                mat[x][y] = i
                i += 1
            top += 1    # update boundary

            # top to bottom
            y = right
            for x in range(top, bottom+1):
                mat[x][y] = i
                i += 1
            right -= 1  # update boundary

            # right to left
            x = bottom
            for y in range(right, left-1, -1):
                mat[x][y] = i
                i += 1
            bottom -= 1 # update boundary

            # bottom to top
            y = left
            for x in range(bottom, top-1, -1):
                mat[x][y] = i
                i += 1
            left += 1   # update boundary

        return mat
