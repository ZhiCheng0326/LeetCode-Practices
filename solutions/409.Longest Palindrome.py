class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashtable = dict()
        ans = 0

        for char in s:
            if char not in hashtable:
                hashtable[char] = 1
            else:
                hashtable[char] += 1

        hasOdd = 0
        for key, value in hashtable.items():
            if value % 2 == 0:
                # if even
                ans += value
            else:
                # if odd, take the even amount (eg:5, add 4 chars)
                ans += int(value//2*2)
                hasOdd = 1

        ans += hasOdd
        return ans
