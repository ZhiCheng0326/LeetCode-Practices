# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head

        cur = head
        length = 1

        # count length of linked list and close loop
        while cur.next:
            cur = cur.next
            length += 1
        cur.next = head

        # move pointer to new tail
        new_tail = head
        for _ in range(length-(k%length)-1):
            new_tail = new_tail.next

        # at this stage, new head = new tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head
