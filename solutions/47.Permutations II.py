class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        def backtrack(path, choices, n):
            # if condition is satisfied, append to ans
            if len(path) == n:
                ans.append(path[:])

            for ind, c in enumerate(choices):
                # to avoid duplicate answer
                if ind-1 >= 0 and choices[ind] == choices[ind-1]: continue

                # choose one element
                path.append(c)

                # backtracking
                backtrack(path, choices[:ind]+choices[ind+1:], n)

                # revert
                path.pop()

        backtrack([], nums, n)
        return ans
