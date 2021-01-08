# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# ## Single traversal method
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         dummy = ListNode(0, head)
#         ptr1 = dummy
#         ptr2 = head

#         for i in range(n):
#             ptr2 = ptr2.next

#         while ptr2:
#             ptr1 = ptr1.next
#             ptr2 = ptr2.next

#         ptr1.next = ptr1.next.next
#         return dummy.next

## Stack method
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        stack = []
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next

        while n >= 0:
            cur = stack.pop()
            n-=1

        cur.next = cur.next.next

        return dummy.next
