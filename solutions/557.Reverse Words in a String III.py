# # Method 1: stop when meet '', then reverse each word
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         start = end = 0
#         self.s = list(s)
#         n = len(self.s)

#         for end in range(n):
#             if self.s[end] == ' ':
#                 self.reverse(start, end-1)
#                 start = end + 1

#         self.reverse(start, end)

#         return ''.join(self.s)

#     def reverse(self, start, end):
#         while start<end:
#             self.s[start], self.s[end] = self.s[end], self.s[start]

#             start += 1
#             end -= 1

# # Method 2: Using python indexing to reverse the string
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         start = end = 0

#         s = list(s)
#         n = len(s)

#         for end in range(n):
#             if s[end] == ' ':
#                 s[start:end] = s[start:end][::-1]
#                 start = end + 1

#         s[start:end+1] = s[start:end+1][::-1]

#         return ''.join(s)

# # Method 3: "abc def" to "fed cba", then ["fed", "cba"] to ["cba", "fed"]
# # This method is faster because no looping through each word
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         s = s[::-1]
#         s = s.split()[::-1]
#         return ' '.join(s)

# Method 4: ["abc", "def"] to ["def", "abc"], then "def abc" to "cba fed"
# This method is faster because no looping through each word
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()[::-1]
        s = ' '.join(s)[::-1]
        return s
