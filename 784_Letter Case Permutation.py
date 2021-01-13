# Method 1, backtracking (slow method, 56ms)
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = []

        def backtrack(path, index):
            # if condition is met, append path to ans
            if index == len(path):
                ans.append("".join(path))
                return

            if path[index].isalpha():
                # make choices and convert target char to lower case
                path = path[:index]+path[index].lower()+path[index+1:]
                index += 1
                # backtracking
                backtrack(path, index)
                # revert
                index -= 1

                # make choices and convert target char to upper case
                path = path[:index]+path[index].upper()+path[index+1:]
                index += 1
                # backtracking
                backtrack(path, index)
                # revert
                index -= 1

            else:
                # make choices
                index += 1
                # backtracking
                backtrack(path, index)
                # revert
                index -= 1

        backtrack(S, 0)
        return ans

# # Method 2, traversal method（36ms）
# class Solution:
#     def letterCasePermutation(self, S: str) -> List[str]:
#         ans = [S]
#         for i in range(len(S)):

#             if S[i].isalpha():
#                 for j in range(len(ans)-1, -1, -1):
#                     # copy the existing answer
#                     ans.append(ans[j])
#                     # convert upper to lower case
#                     if ans[j][i].isupper(): ans[j] = ans[j][:i]+ans[j][i].lower()+ans[j][i+1:]
#                     # convert lower to upper case
#                     else: ans[j] = ans[j][:i]+ans[j][i].upper()+ans[j][i+1:]

#         return ans
