# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            temp = ListNode()
            if l1.val<l2.val:
                temp.val = l1.val
                l1 = l1.next
            else:
                temp.val = l2.val
                l2 = l2.next

            cur.next = temp
            cur = cur.next

        if l1: cur.next = l1
        elif l2: cur.next = l2

        return dummy.next
