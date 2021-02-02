"""
'top', 'bottom', 'left', 'right' to mark upper and lower boundaries of accessing each element in matrix
1) Go right, check if bottom<top, means cannot go down, break the loop
2) Go down, check if right<left, means cannot go left, break the loop
3) Go left, check if bottom<top, means cannot go up, break the loop
4) Go up, check if right<left, means cannot go right, break the loop

Time complexity: O(mn)
Space complexity: O(1)
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        ans = []

        # x loop through rows, y loop through cols
        while True:
            ## x fixed at top row, y go right
            x = top
            for y in range(left, right+1):
                ans.append(matrix[x][y])
            top += 1                # update top
            if bottom < top: break  #'top' index must smaller than 'bottom'

            ## y fixed at right col, x go down
            y = right
            for x in range(top, bottom+1):
                ans.append(matrix[x][y])
            right -= 1              # update right
            if left > right: break  #'left' index must smaller than 'right'

            ## x fixed at bottom row, y go left
            x = bottom
            for y in range(right, left-1,-1):
                ans.append(matrix[x][y])
            bottom -= 1             # update bottom
            if bottom < top: break  #'top' index must smaller than 'bottom'

            ## y fixed at left col, x go up
            y = left
            for x in range(bottom, top-1,-1):
                ans.append(matrix[x][y])
            left += 1               # update left
            if left > right: break  #'left' index must smaller than 'right'

        return ans
