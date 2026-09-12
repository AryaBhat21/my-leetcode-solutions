# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMid(self, head)->Optional[ListNode]:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow 

    def merge2list(self, list1, list2)->Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy
        
        while list1 and list2:
            if list1.val<=list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = self.findMid(head)
        right_head = mid.next
        mid.next = None
        left_head = head

        left_sorted = self.sortList(left_head)
        right_sorted = self.sortList(right_head)

        return self.merge2list(left_sorted, right_sorted)


        
