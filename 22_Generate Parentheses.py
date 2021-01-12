class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(path, left_bracket, right_bracket, n):
            print(path)
            if right_bracket == n:
                ans.append("".join(path))
                return

            if left_bracket < n:
                path.append("(")
                backtrack(path, left_bracket+1, right_bracket, n)
                path.pop()

            if right_bracket < left_bracket:
                path.append(")")
                backtrack(path, left_bracket, right_bracket+1, n)
                path.pop()

        backtrack([], 0, 0, n)
        return ans
