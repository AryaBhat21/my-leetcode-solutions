# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            count+=1
            temp=temp.next
        if count == n:
            return head.next
        steps = count - n
        temp=head
        for i in range(steps-1):
            temp=temp.next
        temp.next = temp.next.next
        return head