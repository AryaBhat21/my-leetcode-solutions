# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        head = l1
        prev = None
        carry = 0
        while l1 and l2 :
            tot = l1.val+l2.val+carry
            l1.val = tot%10
            carry = tot//10
            prev = l1
            l1 = l1.next
            l2 = l2.next
        if l2:
            prev.next = l2
            l1 = l2
        while l1 and carry:
            tot = l1.val+carry
            l1.val = tot%10
            carry = tot//10
            prev = l1
            l1 = l1.next
        if carry:
            prev.next=ListNode(carry)
        return head
            