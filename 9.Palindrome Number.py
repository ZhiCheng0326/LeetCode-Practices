# # Method 1: reverse every digit and compare with initial x
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0: return False

#         copy = x
#         reverse = 0
#         while copy != 0:
#             pop = copy % 10
#             copy = copy // 10
#             reverse = reverse * 10 + pop

#         return reverse == x

# # Method 2: reverse half of the digit and compare with initial x
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x%10==0 and x != 0): return False

        reverse = 0
        # if x > reverse means we have revert half of the digit
        while x > reverse:
            pop = x % 10
            x = x // 10
            reverse = reverse * 10 + pop
        return x == reverse or x == reverse // 10
