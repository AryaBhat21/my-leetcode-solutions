# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        val = []
        temp = head
        while temp:
            val.append(temp.val)
            temp = temp.next
        val.sort()
        temp = head
        i=0
        while temp:
            temp.val = val[i]
            i+=1
            temp = temp.next
        return head
        