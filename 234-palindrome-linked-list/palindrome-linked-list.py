# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev_ll(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        is_palin = True
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        new_head = self.rev_ll(slow.next)

        first = head
        second = new_head

        while second:
            if first.val!=second.val:
                is_palin = False
                break
            first = first.next
            second = second.next
        
        slow.next = self.rev_ll(new_head)

        return is_palin
        
        