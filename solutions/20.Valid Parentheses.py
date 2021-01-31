class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"(":")", "{":"}", "[": "]"}
        stack = []

        # odd length must be False
        if len(s) % 2 != 0: return False

        for char in s:
            # if char is right bracket
            if char not in pair:
                # if there is no left bracket in stack or the brackets do not match
                if len(stack) == 0 or pair[stack[-1]] != char:
                    return False
                stack.pop()

            # if char is left bracket
            else:
                stack.append(char)

        # if there are left brackets remain in stack, means s is not valid
        return len(stack) == 0
