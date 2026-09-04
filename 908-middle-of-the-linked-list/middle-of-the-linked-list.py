# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0 
        temp = head
        while temp is not None:
            count+=1
            temp=temp.next
        
        ind = count//2
        var = 0
        again = head
        while again is not None:
            if ind==var:
                return again
            var+=1
            again=again.next
        