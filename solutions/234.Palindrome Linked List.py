# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Fast slow pointer
"""
1) Move fast slow ptr so that slow.next pointing second half
2) Reverse second half, then check is it palindrome

Time complexity: O(N)
Space complexity: O(1)
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True

        fast = slow = head
        # move 'slow' so that slow.next is the second half
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

        # reverse second half, [slow.next:]
        prev = None
        cur = slow.next
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        # 'prev' is the head of reversed second half, compare first & second half
        while prev and head:
            if prev.val != head.val:
                # return False as it is not palindrome
                return False
            prev = prev.next
            head = head.next

        return True
