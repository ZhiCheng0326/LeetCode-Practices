# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# Method 1: Mid-order traversal (56ms)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.prev = None

        def dfs(node):
            if node is None: return True

            # traverse left tree
            if not dfs(node.left): return False

            # make sure current node.val larger than previous node.val
            if self.prev is not None and node.val<=self.prev: return False
            self.prev = node.val

            # traverse right tree
            if not dfs(node.right): return False

            return True

        return dfs(root)

# # Method 2: Recursive (determine if current node.val within boundaries)(56ms)
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#
#         def dfs(node, lower, upper):
#             if node is None: return True
#
#             if node.val <= lower or node.val >= upper: return False
#
#             if not dfs(node.left, lower, node.val): return False
#             if not dfs(node.right, node.val, upper): return False
#             return True
#
#         return dfs(root,float('-inf'), float('inf'))
