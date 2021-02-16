# # Method 1
# # Time Complexity: O(log n)
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         tmp = 1
#         while tmp <= n:
#             if tmp == n:
#                 return True
#             tmp *= 2
#         return False

# # Method 2
# # Time Complexity: O(1)
# # if "n == 2^x", then "n & (n-1) == 0"
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         return n > 0 and n & (n-1) == 0

# # Method 3
# # Time Complexity: O(1)
# # -n = ~n + 1
# #  n & (-n) return most right '1' of n
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (-n) == n
