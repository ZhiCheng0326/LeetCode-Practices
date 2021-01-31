# # Vertical scanning
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         n = len(strs)
#         if not strs: return ""
#         ans = 0

#         for char_ind in range(len(strs[0])):
#             for words in range(1, n):
#                 if char_ind<=len(strs[words])-1 and strs[words][char_ind] == strs[0][char_ind]:
#                     ans += 1
#                 else:
#                     # strs[words][char_ind] != strs[0][char_ind]
#                     ans = char_ind-1
#                     return strs[0][:ans+1]
#         return strs[0][:ans+1]

# Binary search
# 1) find min length of string in strs
# 2) binary search throgh strs[i_ _ n-1] to find the LCP
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""

        minLength = min(len(s) for s in strs)
        left, right = 0, minLength-1

        while left <= right:
            mid = (left + right) //2
            # if strs[i][:mid+1] is common for all strings in strs, search in right site
            if self.isCommon(strs, mid+1):
                left = mid+1
            else:
                right = mid-1

        return strs[0][:left]

    def isCommon(self, strs, length):
        n = len(strs)
        for word in range(1, n):
            if strs[word][:length] != strs[0][:length]:
                return False
        return True
