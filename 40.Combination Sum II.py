class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def backtrack(path, choices, cur_sum):
            for ind, c in enumerate(choices):
                # avoid duplicate answer
                if ind-1 >= 0 and choices[ind-1] == choices [ind]: continue

                # make choices
                path.append(c)
                cur_sum += c

                # pruning
                if cur_sum > target:
                    cur_sum -=c
                    path.pop()
                    return
                elif cur_sum == target:
                    ans.append(path[:])
                    cur_sum -=c
                    path.pop()
                    return

                # backtracking
                backtrack(path, choices[ind+1:], cur_sum)

                # revert
                cur_sum -=c
                path.pop()

        backtrack([], candidates, 0)
        return ans
