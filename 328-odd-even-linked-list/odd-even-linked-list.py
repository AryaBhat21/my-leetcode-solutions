# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        arr = []
        #append odd indices 
        temp = head
        while temp and temp.next:
            arr.append(temp.val)
            temp=temp.next.next
        # If odd length, the last node was skipped by temp.next check
        if temp:
            arr.append(temp.val)
        #append even indices
        temp = head.next
        while temp and temp.next:
            arr.append(temp.val)
            temp = temp.next.next
        # If even length, the last node was skipped by temp.next check
        if temp:
            arr.append(temp.val)
        #rewrite
        temp = head
        i=0
        while temp:
            temp.val=arr[i]
            i+=1
            temp=temp.next
        return head

        

