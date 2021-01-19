# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Method 1: stack
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ptr = head
        stack = [None] #important!

        while ptr:
            stack.append(ptr)
            ptr = ptr.next

        head = stack.pop()
        cur = head
        while stack:
            cur.next = stack.pop()
            cur = cur.next

        return head

# # Method 2: Double pointer
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         cur = head
#         prev = None

#         while cur:
#             tmp = cur.next # store next node
#             cur.next = prev

#             prev = cur
#             cur = tmp
#         return prev

        
