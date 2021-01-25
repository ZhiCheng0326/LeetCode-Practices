class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        head, tail = 0, n-1

        while head < tail:
            s[head], s[tail] = s[tail], s[head]
            head += 1
            tail -= 1
