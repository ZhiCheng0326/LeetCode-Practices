# # Method 1, use for loop
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         ans = [[]]

#         for i in range(n):
#             c = ans.copy()
#             for sub in c:
#                 ans.append(sub+ [nums[i]])

#         return ans

# Method 2, backtrack
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(cur, path):
            # add result if condition is satisfied
            ans.append(path[:]) # note that use path[:] instead of path

            for i in range(cur, n):
                # choose one element
                path.append(nums[i])
                backtrack(i+1, path)
                # revert
                path.pop()

        backtrack(0,[])
        return ans
