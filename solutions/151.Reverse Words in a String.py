# # Method 1: Using python built-in 'split' and 'join' function
# """
# Time Complexity: O(n)
# Space Complexity: O(n)
# """
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         s = s.split()

#         # reverse whole sentence
#         left, right = 0, len(s)-1

#         while left< right:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1

#         return ' '.join(s)

# Method 2: Write own function
"""
1) Remove leading and trailing spaces, meanwhile removing redundant spaces in between words
2) Reverse whole string
3) Reverse each word
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        self.s = self.removeSpaces(s)
        self.reverseWhole(0, len(self.s)-1)
        self.reverseEach()
        return ''.join(self.s)

    def removeSpaces(self, s):
        left, right = 0, len(s)-1

        # remove leading or trailing spaces
        while left<= right:
            if s[left] == ' ':
                left += 1
            elif s[right] == ' ':
                right -= 1
            else:
                break

        # append each char to tmp meanwhile check for redundant spaces in between words
        tmp = []
        while left <= right:
            if s[left] == ' ' and tmp[-1] == ' ':
                left += 1
                continue
            tmp.append(s[left])
            left += 1
        return tmp

    def reverseWhole(self, left, right):

        while left< right:
            self.s[left], self.s[right] = self.s[right], self.s[left]
            left += 1
            right -= 1

    def reverseEach(self):
        left = right = 0

        # left pointing at first char, right pointing at ' '
        while left < len(self.s):
            while right < len(self.s) and self.s[right] != ' ' :
                right += 1
            self.reverseWhole(left, right-1)
            right += 1
            left = right
