class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def backtrack(path, choices):
            # if a condition is satisfied, append to ans
            if len(path) == n:
                ans.append(path[:])

            for i in range(len(choices)):
                # choose one element from choices
                path.append(choices[i])
                backtrack(path, choices[:i]+choices[i+1:])
                # revert
                path.pop()

        backtrack([], nums)
        return ans
