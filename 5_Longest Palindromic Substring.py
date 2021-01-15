# Method 1: Dynamic programming
## If s[i]==s[j], and s[i+1:j] is palindrome, then s[i:j+1] is palindrome
## If (j-1)-(i+1)+1 < 2, it is palindrome for sure, therefore rearrange and get j-i<3
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2: return s

        dp =[[False]*n for _ in range(n)]

        start = end = 0

        for i in range(n):
            dp[i][i] = True

        for j in range(1,n):
            for i in range(j):
                dp[i][j] = (s[i]==s[j]) and (j-i<3 or dp[i+1][j-1])

                if dp[i][j] and j-i+1 > end-start:
                    start = i
                    end = j

        return s[start:end+1]

# # Method 2: Expand from center
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         start = end = 0

#         for i in range(n):
#             # odd length palindrome
#             left1, right1 = self.expandFromCenter(s,i,i)
#             # even length palindrome
#             left2, right2 = self.expandFromCenter(s,i,i+1)

#             # update longest length
#             if right1 - left1 > end-start:
#                 start = left1
#                 end = right1

#             if right2 - left2 > end-start:
#                 start = left2
#                 end = right2
#         return s[start:end+1]

#     def expandFromCenter(self, s, left, right):
#         n = len(s)
#         while left >= 0 and right < n and s[right] == s[left]:
#             left -= 1
#             right += 1

#         return left+1, right-1
