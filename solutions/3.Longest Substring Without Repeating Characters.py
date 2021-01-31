# Sliding window
"""
if s[right] not in lookup, right += 1 and add char to lookup
if s[right] in lookup, left should be at s[k+1] where k is the repeated char
therefore, keep remove s[left] from lookup until s[right] no longer in lookup
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        n = len(s)
        lookup = set()
        ans = 0

        while right < n:
            # print(left, right)
            if s[right] not in lookup:
                lookup.add(s[right])
                ans = max(ans, right-left+1)
                right += 1

            else:
                while s[right] in lookup:
                    lookup.remove(s[left])
                    left += 1
        return ans
                
