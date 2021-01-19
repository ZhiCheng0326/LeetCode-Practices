# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode(0)
        ptr = dummy

        while l1 or l2:
            l1val = l1.val if l1 is not None else 0
            l2val = l2.val if l2 is not None else 0

            total = l1val + l2val + carry
            carry = total // 10
            val = total % 10

            ptr.next = ListNode(val)
            ptr = ptr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry >0:
            ptr.next = ListNode(carry)

        return dummy.next
