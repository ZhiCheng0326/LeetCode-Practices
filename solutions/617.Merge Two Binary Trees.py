# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        def dfs(t1, t2):
            if not t1:
                return t2
            if not t2:
                return t1

            t3 = TreeNode(t1.val+t2.val)
            t3.left = dfs(t1.left, t2.left)
            t3.right = dfs(t1.right, t2.right)
            return t3

        return dfs(t1, t2)
