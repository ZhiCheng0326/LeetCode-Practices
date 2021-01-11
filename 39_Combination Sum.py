class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        ans = []

        def backtrack(path, choices, cur_sum):
            # cur_sum is the sum of all element in path
            if cur_sum == target:
                # add result if condition is satisfied
                ans.append(path[:])

            for ind, c in enumerate(choices):
                # choose one element
                path.append(c)

                cur_sum += c

                # pruning
                if cur_sum > target:
                    cur_sum -=c
                    path.pop()
                    return

                backtrack(path, choices[ind:], cur_sum) #choices[ind:] is used to avoid selecting element from choices[:ind]

                # revert
                cur_sum -=c
                path.pop()

        backtrack([], candidates, 0)
        return ans
