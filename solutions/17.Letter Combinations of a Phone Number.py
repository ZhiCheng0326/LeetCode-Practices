class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        n = len(digits)
        ans = []

        def backtrack(path, digits, n):
            if len(path) == n:
                ans.append("".join(path))
                return

            for ind, d in enumerate(digits):
                # pruning
                if len(digits) - ind + (len(path)) >= n:
                    for letter in mapping[d]:
                        # make choices
                        path.append(letter)
                        # backtracking
                        backtrack(path, digits[ind+1:], n)
                        # revert
                        path.pop()

        backtrack([], digits, n)
        return ans
