# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1 # visited root node

        def dfs(node):
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)
            self.ans = max(self.ans, l+r+1) # number of visited node = depth_left + depth_right + 1(current node)
            # print(node.val, l+r+1)
            return max(l,r)+1 # return depth from current node

        dfs(root)
        return self.ans-1 # diameter = number of visited node - 1
