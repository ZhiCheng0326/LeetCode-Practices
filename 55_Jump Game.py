# Greedy method
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        furthest = 0
        for ind, step in enumerate(nums):
            if ind <= furthest: # if current ind > furthest it can reach means unreachable
                furthest = max(furthest, step + ind)
                if furthest >= n-1: # if the furthest step is larger than n-1, means it can reach n-1
                    return True
            else:
                break

        return False
