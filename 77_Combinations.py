class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(path, k, min_n, max_n):
            # add result if condition is satisfied
            if len(path) == k:
                ans.append(path[:])
                return

            for i in range(min_n, max_n+1):
                if max_n - i + (len(path)+1) >= k: #pruning, reduce time consumption from 268ms to 48ms
                    # make choices
                    path.append(i)
                    # backtracking
                    backtrack(path, k, i+1, max_n)
                    # revert
                    path.pop()

        backtrack([], k, 1, n)
        return ans
